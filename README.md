# instance-celery-test
## ejemplo simple de como utilizar una instancia de celery.
# Forma de uso:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
sudo docker build -t celery:1.0 . 
sudo docker run --name celery1.0 -v $(pwd)/:/app/ --network="host" celery:1.0 -A proj worker -l info -E
