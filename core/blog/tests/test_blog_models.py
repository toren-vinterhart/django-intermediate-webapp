from django.test import TestCase
from datetime import datetime

from ..models import Post, Category
from accounts.models.users import User
from accounts.models.profiles import Profile


class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        user = User.objects.create_user(
            email="test@test.com",
            password="@test123",
        )
        profile = Profile.objects.create(
            user=user,
            first_name="test_first_name",
            last_name="test_last_name",
            description="test_description",
        )
        category_obj = Category.objects.create(name="test_category")
        post = Post.objects.create(
            author=profile,
            category=category_obj,
            title="test_title",
            content="test_content",
            status=True,
            published_date=datetime.now(),
        )
        self.assertEqual(post.title, "test_title")
        self.assertEqual(post.content, "test_content")
