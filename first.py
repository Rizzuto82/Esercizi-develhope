from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_dag_args = {
    "start_date": datetime(2023,10,11),
    "email_on_failure": False,
    "email_on_retry": False,
    "retryes": 1,
    "retray_delay": timedelta(minutes=5),
    "project_id": 1
}


with DAG ("first_dag", schedule_interval = None, default_args = default_dag_args) as dag:
    task0 = BashOperator(task_id = "bash_task", bash_command = "echo 'command executed from Bash Operator' ")
    task1 = BashOperator(task_id = "bash_task_move_data", bash_command = "cp C:/Users/rizzu/OneDrive/Desktop/airflow/DATA_CENTER/DATA_LAKE/dataset_raw.txt C:/Users/rizzu/OneDrive/Desktop/airflow/DATA_CENTER/CLEAN_DATA")
    task2 = BashOperator(task_id = 'bash_task_remove_data', bash_command = "rm C:\Users\rizzu\OneDrive\Desktop\airflow\DATA_CENTER\DATA_LAKE\dataset_raw.txt"
    
    task0 >> task1 >> task2



