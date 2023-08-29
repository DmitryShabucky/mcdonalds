import time

from celery import shared_task
from time import sleep

@shared_task
def hello():
    sleep(10)
    print("Hello, World!!!")

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)