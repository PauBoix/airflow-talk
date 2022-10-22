from airflow.decorators import task, dag
from airflow.operators.python import PythonOperator
from datetime import datetime

def _process(data_interval_start, data_interval_end, arg1, arg2):
    print(f"Start: {data_interval_start} end: {data_interval_end}!")
    print(f"Received: {arg1} and {arg2}!")

@dag(start_date=datetime(2022, 10, 18), schedule_interval='0 * * * *', catchup=True)
def second_dag():

    @task()
    def task_a():
        pass

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=_process,
        op_kwargs={
            "data_interval_start": "{{ data_interval_start }}",
            "data_interval_end": "{{ data_interval_end }}",
            "arg1": "second_arg",
            "arg2": 2,
        }
    )

    task_a() >> task_b

dag = second_dag()
