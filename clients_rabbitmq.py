
from celery_use_cases import tasks_rabbitmq as trabbit
from celery.result import AsyncResult


asyncobj = trabbit.prepare_hamburger.apply_async(('3', 'small'))
print("Hamburger is ordered")
result = AsyncResult(asyncobj.id, app=trabbit.app)

print(result.get()) # 'return value'

asyncobj = trabbit.prepare_spaghetti.delay('3', 'small')
print("Spaghetti is ordered")
result = AsyncResult(asyncobj.id, app=trabbit.app)
print(result.get()) # 'return value'






