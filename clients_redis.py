
from celery_use_cases import tasks_redis as tredis
from celery.result import AsyncResult


asyncobj = tredis.prepare_frites.apply_async(('3', 'small'))
print("Frites is ordered")
result = AsyncResult(asyncobj.id, app=tredis.app)
print(result.get()) # 'return value'

asyncobj = tredis.prepare_tee.delay('3', 'small')
print("Tee is ordered")
result = AsyncResult(asyncobj.id, app=tredis.app)
print(result.get()) # 'return value'





