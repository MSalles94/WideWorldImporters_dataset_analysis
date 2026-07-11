from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="test_dag",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["teste"],
)
def execute_dag():

    @task
    def hello():
        print("Airflow funcionando!")
        return "sucesso"

    @task
    def process():
        print("Executando processamento")

    resultado = hello()

    process()


execute_dag()