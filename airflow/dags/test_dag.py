from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# DAG 정의
dag = DAG(
    'simple_dag',
    description='간단한 DAG 예제',
    schedule_interval='@once',  # 한 번 실행
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# 간단한 작업 정의
task1 = BashOperator(
    task_id='print_current_time',
    bash_command='date',
    dag=dag
)

# 작업 간의 의존성 정의
task1