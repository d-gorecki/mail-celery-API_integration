from django.core.mail import EmailMessage, get_connection
from celery import shared_task
from celery.signals import task_success, task_failure
from mailservice.models.email import Email
from mailservice.models.mailbox import Mailbox
from datetime import datetime
from django.conf import settings
import os
import logging


@shared_task(bind=True)
def send_email_task(self, mailbox, template, validated_data, filename, email_id):
    try:
        with get_connection(
            host=mailbox.get("host"),
            port=mailbox.get("port"),
            username=mailbox.get("login"),
            password=mailbox.get("password"),
            use_ssl=mailbox.get("use_ssl"),
            use_tls=True,
        ) as connection:
            email = EmailMessage(
                template.get("subject"),
                template.get("text"),
                mailbox.get("email_from"),
                validated_data.get("to"),
                validated_data.get("bcc"),
                cc=validated_data.get("cc"),
                reply_to=[validated_data.get("reply_to")],
                connection=connection,
            )
            email.attach_file(filename)
            email.send()
    except Exception as e:
        logging.error(f"Sending mail {email_id} failed @ {datetime.now()}\n")
        raise self.retry(exc=e, countdown=1, max_retries=2)

    return email_id


@task_success.connect(sender=send_email_task)
def task_success_actions(sender, result, **kwargs):
    email = Email.objects.get(pk=result)
    email.sent_date = datetime.now()
    mailbox = email.mailbox
    mailbox.sent += 1
    mailbox.save()
    email.save()
