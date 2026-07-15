
from datetime import datetime,timedelta
from airflow.decorators import dag,task


default_args={
    'owner':'Matheus',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}
@dag(
    dag_id="docker_manipulation_1",
    default_args=default_args,
    start_date=datetime(2026,7,6,1),
    schedule='@daily'
)
def tasks_definition():
      

    @task.bash()
    def execute_python():
        return """
        docker exec python \
        uv run python /app/python_source/task_scripts/simple_task.py 
        """

 
    execute_python()
  
     

greet_dag=tasks_definition()