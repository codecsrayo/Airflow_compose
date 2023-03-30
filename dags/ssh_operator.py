from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 1, 1),
}

dag = DAG(
    dag_id='ssh',
    default_args=default_args,
    schedule_interval=None,
)

start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

ssh_task = SSHOperator(
    task_id='ssh_task',
    command='sc start demo -s {{var.value.remote_user}}:{{var.value.remote_password}}',
    ssh_conn_id='ssh',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag,
)

start_task >> ssh_task >> end_task