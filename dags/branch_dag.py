from airflow.decorators import task
from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from datetime import datetime

def _branching(data_interval_start, data_interval_end):
    return 'before_noon' if data_interval_start.hour < 12 else 'task_c'

with DAG(
    dag_id = "branch_dag",
    start_date = datetime(2022, 10, 22),
    schedule = '@hourly',
    catchup = True,
) as dag:

    task_branch = BranchPythonOperator(
        task_id="task_branch",
        python_callable=_branching,
    )

    @task(task_id='before_noon')
    def task_b():
        print("Task ran before noon")

    @task()
    def task_c():
        print("Task ran after noon")
    


    task_branch >> task_b()
    task_branch >> task_c()

