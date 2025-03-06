from django.core import management

from TripELD import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
