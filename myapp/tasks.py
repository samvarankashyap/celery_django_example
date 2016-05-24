from celery import task

@task()
def add(x, y):
    return x + y
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
 
logger = get_task_logger(__name__)
 
# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def scraper_example():
    logger.info("Start task")
    now = datetime.now()
    logger.info("Task finished: result = "+str(now))
