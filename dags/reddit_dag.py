from airflow import DAG
from datetime import datetime
from importlib import import_module
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline

PythonOperator = import_module("airflow.operators.python").PythonOperator

default_args = {
    "owner": "Carlos Henrique",
    "start_date": datetime(2020, 5, 26),
}

file_postfix = datetime.now().strftime("%Y%m%d%H%M%S")

dag = DAG(
    dag_id="etl_reddit_pipeline",
    default_args=default_args,
    catchup=False,
    tags={"reddit", "etl", "pipeline"},
)

extract_task = PythonOperator(
    task_id="reddit_extract",
    python_callable=reddit_pipeline,
    op_kwargs={
        "filter_name": f"reddit_{file_postfix}",
        "subreddit": "dataengineering",
        "time_filter": "day",
        "limit": 100,
    },
    dag=dag,
)