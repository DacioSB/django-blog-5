from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='Test Body',
            status=Post.Status.PUBLISHED
        )

    def test_post_list_view_success(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/list.html')

    def test_post_detail_view_success(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/detail.html')
