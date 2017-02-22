# celery_django_example
Example application of celery, implementing async tasks and periodic tasks.
# Installation
pip install django-celery celery celery[redis]

# Running 
python manage.py runserver 0.0.0.0:PORTNO


# to start celery deamon 
python manage.py celeryd --verbosity=2 --loglevel=DEBUG
# to start celery beat service 
python manage.py celerybeat --verbosity=2 --loglevel=DEBUG
# reference links for the scheduled tasks
# http://docs.celeryproject.org/en/master/userguide/calling.html#eta-and-countdown
# install redis , and change the conf file bind address to 0.0.0.0
# after installing redis by default the redis server wont start , manually start by systemctl start redis ..,.,.
# configure setings.py in django to match the redis config
# to check the tasks are working or not 
# use python manage.py shell
## from myapp.tasks import add # add import statement
## result = add.apply_async((2,2),countdown=3)  # this will start the task after 3 seconds where add is a function in tasks.py inside myapp
## inorder to schedule a function for next day 
## from datetime import datetime, timedelta
## tomorrow = datetime.utcnow() + timedelta(days=1)
## add.apply_async((2, 2), eta=tomorrow)
