from airflow import DAG
from airflow.operators.bash import BashOperator

from airflow.utils.dates import days_ago

default_args = {
    'owner': 'test02',
    'start_date': days_ago(1)
}

with DAG(
        'test002',
        default_args=default_args,
        schedule_interval=None,
) as dag:
    t1 = BashOperator(
        task_id='Data preprocessing',
        bash_command='Data_preprocessing.py {{ dag_run.conf["working_path"] if dag_run else "" }}',
    )

    t2 = BashOperator(
        task_id='model structing',
        bash_command='model_struct.py {{ dag_run.conf["working_path"] if dag_run else "" }}',
    )

    t1 >> t2
