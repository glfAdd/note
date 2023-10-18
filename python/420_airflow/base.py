from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.dummy_operator import DummyOperator

from airflow.utils.dates import days_ago

from airflow.operators.python import PythonOperator


def default_options():
    default_args = {
        # 拥有者
        'owner': 'airflow',
        # 第一次开始执行的时间，为 UTC 时间(注意不要设置为当前时间)
        'start_date': days_ago(1),
        # 失败重试次数
        'retries': 1,
        # 失败重试间隔
        'retry_delay': timedelta(seconds=5)
    }
    return default_args


# 定义DAG
def test1(dag):
    t = "echo 'hallo world'"
    # operator 支持多种类型， 这里使用 BashOperator
    task = BashOperator(
        # task_id
        task_id='test1',
        # 指定要执行的命令
        bash_command=t,
        # 指定归属的 dag
        dag=dag
    )
    return task


def hello_world_1():
    current_time = str(datetime.today())
    print('hello world at {}'.format(current_time))


def test2(dag):
    # PythonOperator
    task = PythonOperator(
        task_id='test2',
        python_callable=hello_world_1,  # 指定要执行的函数
        dag=dag)
    return task


def test3(dag):
    task = DummyOperator(task_id='test3', dag=dag)
    return task


with DAG(
        'test_task',  # dag_id
        default_args=default_options(),  # 指定默认参数
        schedule_interval="@once"  # 执行周期
) as d:
    task1 = test1(d)
    task2 = test2(d)
    task3 = test3(d)
    task1 >> task2 >> task3  # 指定执行顺序
