## Implementation of recruitment task for the position of backend developer
### _Tech-stack: Python, Django, Django REST framework, PostgreSQL, Celery, redis, Docker, docker-compose_

## Task objective

Create a REST API that allows to send emails:
* to any addresses,
* with the content and theme defined in the Template (Template model from the database),
* from a previously defined mailbox (Mailbox model from the database).

## Tools required

* Python >= 3.10,
* Django, DRF
* PostgreSQL,
* django-environ,
* django-filter,
* celery,
* GIT,

## Functional requirements

* RESTful service architecture,
* database configuration should be stored in a package supported by django-environ,
* the message should be sent from the mailbox specified in the message creation form,
* sending a message possible only from the active mailbox,
* sending messages should be carried out in the Celery task within the same application,
* maximum number of message sending attempts: 3,
* the ability to filter messages by: sent status (state of completion of the sent_date column of the Email model), creation date,
* project code provided by remote repository,

## Required endpoints

| Method      | URL         |Comment      |
| ----------- | ----------- | ----------- |
| GET, POST      | api/mailbox/       | Mailboxes             |
| GET, PUT, PATCH, DELETE   | api/mailbox/:id/        | Mailbox |
| GET, POST | api/template/ | Templates |
| GET, PUT, PATCH, DELETE | api/template/:id/ | Template |
| GET, POST | api/email/ | Browse&send email |
