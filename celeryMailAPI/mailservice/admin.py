from django.contrib import admin
from mailservice.models.email import Email
from mailservice.models.mailbox import Mailbox
from mailservice.models.template import Template

# Register your models here.

admin.site.register(Email)
admin.site.register(Mailbox)
admin.site.register(Template)
