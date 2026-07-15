from airflow.sdk import dag
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime


@dag(
    dag_id="run_python_container",
    start_date=datetime(2026, 7, 15),
    schedule="@daily",
    catchup=False
)
def run_python_container():

    run_pipeline = DockerOperator(
        task_id="execute_python_pipeline",
        image="data_pipeline",
        command="python python_source/main.py",
        docker_url="unix://var/run/docker.sock"
    )


run_python_container()