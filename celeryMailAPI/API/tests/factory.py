import factory
from factory import Faker

from mailservice.models.email import Email
from mailservice.models.template import Template
from mailservice.models.mailbox import Mailbox
from datetime import datetime


class MailboxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mailbox

    id = Faker("uuid4")
    host = "smtp.gmail.com"
    port = 587
    login = "djangomaintenanceapp@gmail.com"
    password = "zaq12wsx"
    email_from = "djangomaintenanceapp@gmail.com"
    date = datetime.now()
    last_update = datetime.now()
    use_ssl = False
    is_active = True


class TemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Template

    id = Faker("uuid4")
    subject = "Test"
    text = "Test"
    attachment = None


class EmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Email

    id = Faker("uuid4")
    mailbox = factory.SubFactory(MailboxFactory)
    template = factory.SubFactory(TemplateFactory)
    to = ["test@gmail.com"]
    reply_to = "test@gmail.com"
    date = datetime.now().date()
    sent_date = datetime.now()
