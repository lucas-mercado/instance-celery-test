sudo docker run --name celery1.1 -v $(pwd)/:/app/ --network="host" lmercado/celery:1.0 -A proj worker -l info -E
