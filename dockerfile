FROM apache/airflow:latest

USER root
RUN apt-get update && apt-get install -y ssh sshpass
RUN pip3 install apache-airflow psycopg2-binary