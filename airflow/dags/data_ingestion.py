
from datetime import datetime,timedelta
from airflow.decorators import dag,task


default_args={
    'owner':'Matheus',
    'retries':0,
    'retry_delay':timedelta(minutes=0)
}
@dag(
    dag_id="data_ingestion",
    default_args=default_args,
    start_date=datetime(2026,7,6,1),
    schedule='@daily'
)
def tasks_definition():

    @task.bash()
    def execute_python(logical_date):
       
        script_path='python_source.task_scripts.ingestion'
        return f"""
        docker exec python \
        bash -c "cd /app && uv run python -m {script_path} \
            --logical_date {logical_date.isoformat()}"
        """

 
    execute_python()
  
     

greet_dag=tasks_definition()