import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id = "docker_dag",
    start_date = datetime.datetime(2022, 10, 22),
    schedule = '@hourly',
    catchup = True,
) as dag:

    task_docker = DockerOperator(
        task_id="task_docker",
        image = 'bitcoin_image:latest',
        command = 'python3 bitcoin_data.py "{{ data_interval_start }}" "{{ data_interval_end }}"',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        auto_remove = True,
    )
