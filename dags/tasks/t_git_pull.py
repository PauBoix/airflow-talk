from airflow import DAG
from airflow.operators.python import PythonOperator
import os

def _process(path):
    os.system(f"git -C {path} pull")

def build_git_pull_task(dag: DAG, path) -> PythonOperator:
    git_pull_task = PythonOperator(
        task_id='git_pull_task',
        python_callable=_process,
        op_args = [path],
    )

    return git_pull_task