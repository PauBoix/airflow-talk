import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id = "docker_dag",
    start_date = datetime.datetime(2022, 10, 22),
    schedule = '@hourly',
    catchup = True,
) as dag:

    def get_bitcoin_price(data_interval_start, data_interval_end):

        import yfinance as yf

        data = yf.download(tickers='BTC-USD', start=data_interval_start, end=data_interval_end, interval = '1m')
        print(data)

    task_docker = DockerOperator(
        task_id="task_docker",
        container_name="",
        image = '',
        command = 'python3 bitcoin_data.py "{{ data_interval_start }}" "{{ data_interval_end }}"'
        network_mode='bridge',
        auto_remove = True,
    )
