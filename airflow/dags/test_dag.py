
from datetime import datetime,timedelta
from airflow.decorators import dag,task


default_args={
    'owner':'Matheus',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}
@dag(
    dag_id="task_flow_api_v1",
    default_args=default_args,
    start_date=datetime(2026,7,6,1),
    schedule='@daily'
)
def tasks_definition():
    
    @task()
    def get_first_name():
        return "Matheus"
    @task()
    def get_last_name():
        return "Salles"
    
    @task()
    def get_age():
        return 31

    @task()
    def greet(first_name,last_name,age):
        print(f"""
        Hello world, this is the mensage:
        my name is {first_name} {last_name} and I'm {age} years old.""")    

    @task.bash()
    def bash_comand(first_name):
        return f"echo Hello World, this is bash. My name: {first_name}."
    
    first_name=get_first_name()
    last_name=get_last_name()
    age=get_age()
     

    greet(first_name,last_name,age)
    bash_comand(first_name)

greet_dag=tasks_definition()