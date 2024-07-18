from celery import Celery
from celery.schedules import crontab


# Create a Celery instance with a Redis broker
app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# Configure Redbeat as the scheduler
app.conf.update(
    redbeat_redis_url='redis://localhost:6379/0',
    beat_scheduler='redbeat.RedBeatScheduler',
)


@app.task
def send_reminder(message):
    print(f"Reminder: {message}")
    return f"Reminder sent: {message}"


# Configure periodic tasks
app.conf.beat_schedule = {
    'send-reminder-every-10-minutes': {
        'task': 'tasks.send_reminder',
        'schedule': crontab(minute='*/10'),  # Every 10 minutes
        'args': ('This is your 10-minute reminder!',)
    },
}


app.conf.timezone = 'Europe/Berlin'
