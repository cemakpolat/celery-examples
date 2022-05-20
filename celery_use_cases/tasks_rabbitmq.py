"""
@author: Cem Akpolat
@created by cemakpolat at 2022-05-18
"""

from time import sleep
from celery import Celery


BACKEND_URL = "rpc://"
BROKER_URL = "pyamqp://guest@localhost//"

# Creating a celery instance with redis as message broker.

app = Celery('tasks', backend=BACKEND_URL, broker=BROKER_URL)


app.conf.task_routes = {
 'celery_use_cases.tasks_rabbitmq.prepare_hamburger': {'queue': 'hamburger'},
 'celery_use_cases.tasks_rabbitmq.prepare_spaghetti': {'queue': 'spaghetti'}
}


@app.task
def prepare_hamburger(table_num, size):

 print('Preparing for the table {}  a {}-sized hamburger!'.format(table_num, size))
 sleep(5)
 return "hamburger"

@app.task
def prepare_spaghetti(table_num, size):

 print('Preparing for the table {}  a {}-sized spaghetti!'.format(table_num, size))
 sleep(6)
 return "spagetti"
