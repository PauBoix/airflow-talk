from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "sensor_dag",
    start_date = datetime(2022, 10, 23),
    schedule = '@hourly',
    catchup = True,
) as dag:

    task_sensor = ExternalTaskSensor(
        task_id="task_sensor",
        external_dag_id='branch_dag',
        external_task_id='before_noon',
        allowed_states=['success'],
        failed_states=['failed', 'skipped'],
    )

    task_b = BashOperator(
        task_id='task_b',
        bash_command='pwd',
        #bash_command='ls -lrt',
        #cwd = '/Documents/test'
    )
    task_sensor >> task_b

