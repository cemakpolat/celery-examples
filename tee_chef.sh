#!/bin/sh

celery -A celery_use_cases.tasks_redis worker -l info -Q tee