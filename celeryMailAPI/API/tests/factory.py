import factory
from factory import Faker

from mailservice.models.email import Email
from mailservice.models.template import Template
from mailservice.models.mailbox import Mailbox


class MailboxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mailbox

    id = Faker("uuid4")
    host = "smtp.gmail.com"
    port = 587
    login = "djangomaintenanceapp@gmail.com"
    password = "zaq12wsx"
    email_from = "djangomaintenanceapp@gmail.com"
    use_ssl = False
    is_active = True


class TemplateFactory(factory.django.DjangoModelFactory):
    pass


class EmailFactory(factory.django.DjangoModelFactory):
    pass
