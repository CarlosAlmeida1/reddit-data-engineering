FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER airflow
RUN pip install --no-cache-dir --user -r /opt/airflow/requirements.txt
