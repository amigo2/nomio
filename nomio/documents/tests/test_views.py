from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from nomio.documents.models import Document


class IndexTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.user = User.objects.create()
        self.client.force_login(self.user)

    def test_redirects_to_login_url_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse("documents:index"))
        self.assertRedirects(response, f"{settings.LOGIN_URL}?next=/documents/")

    def test_get_shows_index_page(self):
        response = self.client.get(reverse("documents:index"))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "documents/index.html")

    def test_invalid_post_shows_index_page_with_form_errors(self):
        response = self.client.post(reverse("documents:index"), {})

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "documents/index.html")
        self.assertNotEqual({}, response.context["form"].errors)

    def test_valid_post(self):
        response = self.client.post(
            reverse("documents:index"),
            {"files": [SimpleUploadedFile("test.txt", b"Hello, world!")]},
        )

        with self.subTest("shows_index_page_with_no_form_errors"):
            self.assertEqual(200, response.status_code)
            self.assertTemplateUsed(response, "documents/index.html")
            self.assertEqual({}, response.context["form"].errors)

        with self.subTest("updates_database"):
            document = Document.objects.last()
            self.assertEqual(self.user, document.creator)
            self.assertEqual("test.txt", document.title)
            self.assertEqual(b"Hello, world!", document.file.read())
