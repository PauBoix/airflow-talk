from tasks.t_git_pull import build_git_pull_task
import datetime
from airflow import DAG
from airflow.models import Variable

with DAG(
    dag_id = "pull_dag",
    start_date = datetime.datetime(2022, 10, 22),
    schedule = '@daily',
    catchup = True,
) as dag:
    task_pull = build_git_pull_task(dag=dag, path=Variable.get("pau_path"))
    task_pull