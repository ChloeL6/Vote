import os
from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor
from airflow.hooks.filesystem import FSHook
from collections import Counter

# global variable for votes file name and valid votes 
VOTES_FILE_NAME = "votes.csv"
FLAVOR_CHOICES  = ["lemon", "vanilla", "chocolate", "pistachio", "strawberry", "confetti", "caramel", "pumpkin", "rose"]


@task
def read_file():
    """
    read votes file from a CSV
    This function uses an Airflow FileSystem Connection called "data_fs" as the root folder
    to look for the votes file. Make sure this FileSystem connection exists
    """
    valid_votes = []
    # get the data_fs filesystem root path
    data_fs = FSHook(conn_id='data_fs')     # get airflow connection for data_fs
    data_dir = data_fs.get_path()           # get its root path
    print(f"data_fs root path: {data_dir}")

    # create the full path to the votes file
    file_path = os.path.join(data_dir, VOTES_FILE_NAME)
    print(f"reading file: {file_path}")

    # read csv and choose valid votes:
    votes = pd.read_csv(file_path, header=1)
    for option in votes:
      if option in FLAVOR_CHOICES:
        valid_votes.append(option)
    return valid_votes

@task
def chosen_flavor(lst):
    count_flavor = Counter(lst)
    highest_vote = max(count_flavor)
    print(f"The number of votes for each flavor are: {count_flavor}, and the winner is {highest_vote}")  

@dag(
    schedule_interval="@once",
    start_date=datetime.utcnow(),
    catchup=False,
    default_view='graph',
    is_paused_upon_creation=True,
    tags=['dsa', 'dsa-code-review'],
)

def cake_flavor():
    """Example of using FileSensors and FileSystem Connections"""

    # define the file sensor...
    # wait for the votes file in the "data_fs" filesystem connection
    wait_for_file = FileSensor(
        task_id='wait_for_file',
        poke_interval=15,                   # check every 15 seconds
        timeout=(30 * 60),                  # timeout after 30 minutes
        mode='poke',                        # mode: poke, reschedule
        filepath=VOTES_FILE_NAME,        # file path to check (relative to fs_conn)
        fs_conn_id='data_fs',               # file system connection (root path)
    )

    # read the file
    read_file_task = read_file()

    #choose flavor with the most votes
    chosen_flavor_task = chosen_flavor(read_file_task)
    
    # orchestrate tasks
    wait_for_file >> read_file_task >> chosen_flavor_task


# create the dag
dag = cake_flavor()