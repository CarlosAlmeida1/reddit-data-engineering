FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
# install build deps as root (needed for compiling some packages)
RUN apt-get update && apt-get install -y gcc python3-dev

# switch to the non-root airflow user and install Python packages into the user's home
# using --user to avoid running pip as root (the official image recommends that)
USER airflow
RUN pip install --no-cache-dir --user -r /opt/airflow/requirements.txt
