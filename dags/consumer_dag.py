from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

dataset = Dataset("/tmp/myfile.txt")

with DAG(
    dag_id= 'consumer_dag',
    schedule=[dataset],
    start_date= datetime(2022, 1, 1),
    catchup = False,
):

    @task()
    def read_dataset():
        with open('/tmp/my_file.txt', 'r') as f:
            print(f.read())

    read_dataset()