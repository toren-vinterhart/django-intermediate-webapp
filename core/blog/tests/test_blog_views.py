from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime

from ..models import Post, Category
from accounts.models import User, Profile


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_url_successful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(str(response.content).find("Test"), -1)
        self.assertTemplateUsed(response, template_name="test.html")


class TestPostDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@test.com", password="@test123")
        self.profile = Profile.objects.get(user__email="test@test.com")
        self.category = Category.objects.create(name="test_category")
        self.post = Post.objects.create(
            author=self.profile,
            category=self.category,
            title="test_title",
            content="test_content",
            status=True,
            published_date=datetime.now(),
        )

    def test_post_detail_view_logged_in_user_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_anonymous_user_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
