from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

dataset = Dataset("/tmp/myfile.txt")

with DAG(
    dag_id= 'producer_dag',
    schedule= '@daily',
    start_date= datetime(2022, 1, 1),
    catchup = False,
):

    @task(outlets=[dataset])
    def update_dataset():
        with open('/tmp/my_file.txt', 'a') as f:
            f.write('producer update')

    update_dataset()