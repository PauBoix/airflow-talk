import datetime
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

def get_bitcoin_price(data_interval_start, data_interval_end):
    import yfinance as yf
    print(data_interval_start)
    print(data_interval_end)
    data = yf.download(tickers='BTC-USD', start=data_interval_start, end=data_interval_end, interval = '1m')
    print(data)

with DAG(
    dag_id = "virtualenv_dag",
    start_date = datetime.datetime(2022, 10, 22),
    schedule = '@hourly',
    catchup = True,
) as dag:
    # @task.virtualenv(
    #     task_id="virtualenv_python",
    #     requirements=["yfinance"],
    #     system_site_packages=True,
    #     provide_context=True,
    #     # op_kwargs={
    #     #     "data_interval_start": "{{ data_interval_start }}",
    #     #     "data_interval_end": "{{ data_interval_end }}",
    #     # },
    #     # op_args=["{{ data_interval_start }}", "{{ data_interval_end }}"],
    # )


    task_virtualenv = PythonVirtualenvOperator(
        task_id="task_virtualenv",
        python_callable=get_bitcoin_price,
        requirements=["yfinance"],
        system_site_packages=True,
        # op_kwargs={
        #     "data_interval_start": "{{ data_interval_start }}",
        #     "data_interval_end": "{{ data_interval_end }}",
        # },
    )
