from dataclasses import dataclass

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.datastructures import MultiValueDict

from nomio.documents.forms import UploadDocumentForm

test_file = SimpleUploadedFile("test.txt", b"Hello, world!")


@dataclass
class MockRequest:
    user: User
    FILES: MultiValueDict


class UploadDocumentFormTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create()
        self.request = MockRequest(
            user=self.user, FILES=MultiValueDict({"files": [test_file]})
        )

    def test_is_not_valid_if_files_not_given(self):
        form = UploadDocumentForm(..., files=MultiValueDict())
        self.assertFalse(form.is_valid())

    def test_is_valid_otherwise(self):
        form = UploadDocumentForm(self.request, files=self.request.FILES)
        self.assertTrue(form.is_valid())

    def test_save_creates_document(self):
        form = UploadDocumentForm(self.request, files=self.request.FILES)
        self.assertTrue(form.is_valid())
        documents = form.save()

        self.assertEqual(1, len(documents))

        document = documents[0]
        self.assertEqual(self.user, document.creator)
        self.assertEqual("test.txt", document.title)
        self.assertEqual(b"Hello, world!", document.file.read())
