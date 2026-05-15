from django.test import (
    TestCase, 
    # SimpleTestCase
)
from django.urls import reverse, resolve
from ..views import IndexView, PostListView, PostDetailView

# Create your tests here.


# TestCase creates a test database that destroys it after completing test
class TestUrl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse("blog:index")
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post-list")
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)


# SimpleTestCase do not create test database
# class TestUrl(SimpleTestCase):
#     def test_blog_index_url_resolve(self):
#         url = reverse("blog:index")
#         self.assertEquals(resolve(url).func.view_class, IndexView)
