
from time import sleep
from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

app = Celery('tasks_redis', backend=BACKEND_URL, broker=BROKER_URL)

app.conf.task_routes = {
    'celery_use_cases.tasks_redis.prepare_tee': {'queue': 'tee'},
    'celery_use_cases.tasks_redis.prepare_frites': {'queue': 'frites'}
}


@app.task
def prepare_tee(table_num, size):

 print('Preparing for the table {}  a {}-sized tee!'.format(table_num, size))
 sleep(2)
 return "tee"


@app.task
def prepare_frites(table_num, size):

 print('Preparing for the table {}  a {}-sized frites!'.format(table_num, size))
 sleep(6)
 return "frites"