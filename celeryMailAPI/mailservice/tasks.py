import os.path
from django.core.mail import EmailMessage, get_connection
from celery import shared_task
from celery.utils.log import get_task_logger


@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3})
def send_email_task(self, mailbox, template, validated_data, filename):

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
