# Vote

#### By Chloe (Yen Chi) Le

#### For this repo, I used Airflow to plan a party 

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
  <img src="/img/DAG.png" width="800"/> 
</p>

Create a DAG and choose flavor has the most votes

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
* Fetch and create .env file:
  ```bash
  curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ```
* Create connection file in airflow: data_fs
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
