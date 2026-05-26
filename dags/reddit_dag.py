from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.providers.standard.operators.python import PythonOperator
from structlog.tracebacks import extract

sys.path.insert(0, os.path(os.path.dirname(os.path.abspath(__file__))))
default_args = {
    'owner': 'Carlos Henrique',
    'start_date': datetime(2020, 5, 26),
}

file_postfix = datetime.now().strftime("%Y%m%d%H%M%S")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl', 'pipeline']
)

extract = PythonOperator(
    task_id='reddit_extract',
    python_callable=reddit_pipeline,
    op_args={
        'file_name': f'reddit_{file_postfix}',
        'subreddit' : 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
)