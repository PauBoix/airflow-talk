import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def _process(arg1, arg2, data_interval_start, data_interval_end):
    print(f"Start: {data_interval_start} end: {data_interval_end}!")
    print(f"Received: {arg1} and {arg2}!")

with DAG(
    dag_id = "first_dag",
    start_date = datetime.datetime(2022, 10, 23),
    schedule = '@hourly',
    catchup = False,
) as dag:
    task_a = PythonOperator(
        task_id="task_a",
        python_callable=_process,
        op_args=["first_arg", 1],
    )