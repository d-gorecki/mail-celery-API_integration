import os.path
from django.core.mail import EmailMessage, get_connection
from celery import shared_task
from celery.utils.log import get_task_logger


def send_email_task(mailbox, template, validated_data):
    with get_connection(
        host=mailbox.host,
        port=mailbox.port,
        username=mailbox.login,
        password=mailbox.password,
        use_ssl=mailbox.use_ssl,
        use_tls=True,
    ) as connection:
        email = EmailMessage(
            template.subject,
            template.text,
            mailbox.email_from,
            validated_data.get("to"),
            validated_data.get("bcc"),
            cc=validated_data.get("cc"),
            reply_to=[validated_data.get("reply_to")],
            connection=connection,
        )
        email.attach_file(template.filename())
        email.send()
