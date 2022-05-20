
#Celery Examples
Install celery

`pip install celery`

## Use case based on Redis

run redis docker

```redis
 docker run --name my-redis -p 6379:6379 --restart always --detach redis
 ```
 
run for redis use cases celery workers
```
./tee_chef.sh
./frites_chef.sh
```

execute redis client 

`python clients_redis.py`


## Use case based on Rabbitmq

run rabbitmq docker

```rabbitmq
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```


run for rabbitmq use cases celery workers

```
./hamburger_chef.sh
./spaghetti_chef.sh
```

execute rabbitmq client

`python clients_rabbitmq.py`