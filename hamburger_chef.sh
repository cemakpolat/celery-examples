#!/bin/sh

celery -A celery_use_cases.tasks_rabbitmq worker -l info -Q hamburger