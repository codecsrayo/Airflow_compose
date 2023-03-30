from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import time
import logging

default_args = {
    'owner': 'Mercadeo',
    'start_date': datetime(2021, 1, 1),
}

dag = DAG(
    dag_id='ssh_v2',
    default_args=default_args,
    schedule_interval=None,
)

start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

ssh_task = SSHOperator(
    task_id='ssh_task',
    command='powershell Start-Service demo',
    ssh_conn_id='ssh',
    dag=dag,
)

def check_service_status(**kwargs):
    ssh_hook = SSHHook(ssh_conn_id='ssh')
    ssh_conn = ssh_hook.get_conn()

    check_status_command = 'powershell (Get-Service demo).Status'

    while True:
        stdin, stdout, stderr = ssh_conn.exec_command(check_status_command)
        status_output = stdout.read().decode('utf-8').strip()

        if status_output == 'Stopped':
            logging.info("Service has stopped.")
            break

        logging.info(f"Service status is {status_output}. Retrying in 10 seconds.")
        time.sleep(10)


check_status_task = PythonOperator(
    task_id='check_status_task',
    python_callable=check_service_status,
    provide_context=True,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag,
)

start_task >> ssh_task >> check_status_task >> end_task
