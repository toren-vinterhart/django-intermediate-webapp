from django.test import TestCase
from datetime import datetime

from ..forms import PostModelForm
from ..models import Category

class TestPostModelForm(TestCase):
    def test_post_model_form_with_valid_data(self):
        category_obj = Category.objects.create(name="ai")
        form = PostModelForm(data={
            "title": "test",
            "content": "description",
            "status": True,
            "category": category_obj,
            "published_date": datetime.now(),
        })
        self.assertTrue(form.is_valid())

    def test_post_model_form_with_no_data(self):
        form = PostModelForm(data={})
        self.assertFalse(form.is_valid())