#!/bing/bash

cd airflow

# make airflow mount dirs
mkdir ./logs ./plugins

# download the docker-compose.yaml and set the .env
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml' > docker-compose.yaml
echo "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
