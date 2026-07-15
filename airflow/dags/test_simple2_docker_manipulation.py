
from datetime import datetime,timedelta
from airflow.decorators import dag,task


default_args={
    'owner':'Matheus',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}
@dag(
    dag_id="docker_manipulation_2",
    default_args=default_args,
    start_date=datetime(2026,7,6,1),
    schedule='@daily'
)
def tasks_definition():
      

 
    @task.bash()
    def execute_python():
        return """
        docker exec python \
        bash -c "cd /app && uv run python -m python_source.task_scripts.task_script_test"
        """

 
    execute_python()
  
     

greet_dag=tasks_definition()