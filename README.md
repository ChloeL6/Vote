# Airflow

#### By Chloe (Yen Chi) Le

#### A DAG to choose cake flavor

<br>

## Technologies Used

* Airflow
* Docker
* Python
* Pandas
* Git
* Markdown
* `.gitignore`
* `requirements.txt`
  
</br>

## Description
<p align="center">
  <img src="/img/DAG_2.png" width="800"/> 
</p>
For this DAG, I used (*FileSensor*) along with (*File Sytem Connection*). The (*Sensor*) will periodically check if a file is created inside a folder. If it is, the downstream tasks will be triggered. (**Connections**) is used for storing essential information that are used by many Tasks. In this case, we will create a file path for our `data/` folder. The instruction for this is in the (**Setup**) section.
 

## Setup/Installation Requirements

* For this repo, Docker Desktop is required. Please install `docker-compose` if you haven't. Follow [their installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) to set it up locally.

* Then open your terminal. Direct to where ever you want to save this repo using:
    ```bash
    cd <your_path>
    ```
* Then clone the repository by inputting: 
  ```bash
  git clone https://github.com/ChloeL6/Vote.git
  ```
* Once everything is cloned, direct to the cloned folder:
  ```bash
  cd vote
  ```
* Once in the correct directory, you will need to set up a virtual environment and activate it in your terminal:
  ```bash
  python3.7 -m venv venv
  source venv/bin/activate
  ```
* After virtualenv is activated, run the command below to install all requirements:
  ```bash
    ./setup.sh
  ```
* With your virtual environment now enabled with proper requirements, open the directory:
  ```bash
  code .
  ```
* Within the `airflow` directory, fetch the latest `docker-compose.yaml` using `curl`, create required subdirectories, and set user id: 
  ```bash
  cd airflow
  curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
  mkdir ./logs ./plugins
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ```
* Once `docker-compose.yaml` file is created, we need to add `/data` under volumes:
<p align="center">
  <img src="/img/volume.png" width="800"/> 
</p>
  
* To initialize airflow, run:
  ```bash
  docker-compose up airflow-init
  ```
* Once initialized, we can start the rest of our containers with:
  ```bash
  docker-compose up
  ```
* When you see the AIRFLOW word in your terminal, that means everything is set up correctly:
  
<p align="center">
  <img src="/img/airflow_setup.png" width="800"/> 
</p>
Leave this running, and open a new terminal tab to use the command line.

* Then navigate to `http://0.0.0.0:8080/home` in your browser and log in as the default user `airflow` with password also  `airflow`.
  
* As mentioned above, (**Connections**) need to be defined in Airflow. Here is how to do it:
    1. Navigate to the Airflow Admin > Connections page
    2. Click the + to add a new Connection
    3. Enter the following information and leave the other fields blank:
        A. (**Connection Id**) = data_fs
        B. (**Connection Type**) = File (path)
        C. (**Extra**) = {"path": "/data"}
    4. Click Save

<p align="center">
  <img src="/img/connection.png" width="800"/> 
</p>

* Once (**Connections**) is created, open DAGs tab, choose `cake_flavor` DAG and trigger it.

* `wait for file` task will keep running and looking for `votes.csv` file until it created. To do that, in your terminal, change to `data` subdirectory and run the following command to download the file:
```bash
  ./get_data
```
* Go back to Airflow, you'll see the `wait_for_file` task is now successful and the next task will be running. Once all tasks are in dark green, that means the DAG has been successfully run.
<p align="center">
  <img src="/img/DAG_2.png" width="800"/> 
</p>

* To see the final output, click on `chosen_flavor` task and go to the `Log`
<p align="center">
  <img src="/img/Log.png" width="800"/> 
</p>

* To stop docker fro running and delete all volumes, run:
  ```bash
   docker-compose down --volumes --remove-orphans
  ```

## Known Bugs

* No known bugs

<br>

## License

MIT License

Copyright (c) 2022 Chloe (Yen Chi) Le

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</br>
