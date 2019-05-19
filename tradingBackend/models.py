from django.db import models
from django_mongoengine import Document, EmbeddedDocument, fields
import datetime

class ExchangeData(Document):
    open_time= fields.IntField()
    close_time = fields.IntField()
    price = fields.IntField()
    value = fields.IntField()
    exchnage = fields.StringField(max_length=255)
    updated = fields.DateTimeField(default=datetime.datetime.utcnow)