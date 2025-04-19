from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime                 import datetime

from tasks.merge import merge
from tasks.drop_duplicates import drop_duplicates
from tasks.clean_reviews import clean_reviews
from tasks.tokenize_reviews import tokenize_reviews
from tasks.remove_stopwords import remove_stopwords
from tasks.stem_tokens import stem_tokens
from tasks.remove_short_words import remove_short_words
from tasks.convert_sentiment import convert_sentiment
from tasks.split import split
from tasks.vectorize_reviews import vectorize_reviews

with DAG(
    dag_id="preprocessing_dag",
    start_date=datetime(2025, 4, 19),
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=False,
    tags=["nlp", "preprocessing"],
) as dag:
    t1  = PythonOperator(task_id="merge"             , python_callable=merge)
    t2  = PythonOperator(task_id="drop_duplicates"   , python_callable=drop_duplicates)
    t3  = PythonOperator(task_id="clean_reviews"     , python_callable=clean_reviews)
    t4  = PythonOperator(task_id="tokenize_reviews"  , python_callable=tokenize_reviews)
    t5  = PythonOperator(task_id="remove_stopwords"  , python_callable=remove_stopwords)
    t6  = PythonOperator(task_id="stem_tokens"       , python_callable=stem_tokens)
    t7  = PythonOperator(task_id="remove_short_words", python_callable=remove_short_words)
    t8  = PythonOperator(task_id="convert_sentiment" , python_callable=convert_sentiment)
    t9  = PythonOperator(task_id="split"             , python_callable=split)
    t10 = PythonOperator(task_id="vectorize_reviews" , python_callable=vectorize_reviews)

    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8 >> t9