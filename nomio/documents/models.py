from django.contrib.auth.models import User
from django.db.models import CharField, Model, ForeignKey, FileField, CASCADE


class Document(Model):
    title = CharField(max_length=255)
    creator = ForeignKey(User, on_delete=CASCADE)
    file = FileField()
    document_sha1 = CharField(max_length=40, blank=False, null=False)
