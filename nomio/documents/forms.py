from typing import List

from django.forms import Form, FileField, FileInput
from django.http import HttpRequest

from .models import Document
from .scripts import generate_sha


class UploadDocumentForm(Form):
    files = FileField(widget=FileInput(attrs={"multiple": True}))

    def __init__(self, request: HttpRequest, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, ) -> List[Document]:
        # https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/#uploading-multiple-files
        for file in self.request.FILES.getlist("files", []):
            sha1 = generate_sha(file)
            file_sha1_object = Document.objects.filter(document_sha1=sha1)

            if file_sha1_object.exists():
                file_sha1_object.delete()

        return [
            Document.objects.create(
                creator=self.request.user,
                title=file.name,
                file=file,
                document_sha1=generate_sha(file),
            )
            for file in self.request.FILES.getlist("files", [])
        ]
