from django.db import models
import mongoengine

class Maxim(mongoengine.Document):
    category = mongoengine.StringField(required=True)
    tag = mongoengine.StringField(required=True)
    content = mongoengine.StringField(required=True)
    interpret = mongoengine.StringField()
    meta = {'db_alias': 'maxim', 'collection':"geyan"}

