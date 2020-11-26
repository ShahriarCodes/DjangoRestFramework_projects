from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

# Create your tests here.
class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1',
            password='123456789'
            )

        test_post = Post.objects.create(
            category_id=1,
            title='Test title',
            excerpt='This is a test post excerpt',
            content='Test post content',
            slug='post-title',
            author_id=1,
            status='published'
            )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = str(post.author)
        excerpt = str(post.excerpt)
        title = str(post.title)
        content = str(post.content)
        status = str(post.status)

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Test title')
        self.assertEqual(excerpt, 'This is a test post excerpt')
        self.assertEqual(content, 'Test post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test title') # __str__
