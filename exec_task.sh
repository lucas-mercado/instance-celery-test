#tendria que crear un entorno donde tendriamos redis, django y celery 
#en la maquina host

source ../.env/bin/activate

python proj/manage.py shell

# En el shell deberiamos correr esta linea para probar
# from proj.tasks import suma
# t = suma.delay(2,2)