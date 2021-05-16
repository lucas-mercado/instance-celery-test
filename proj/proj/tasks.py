from celery import shared_task

@shared_task
def suma(a, b):
	import time
	time.sleep(30)
	return a + b