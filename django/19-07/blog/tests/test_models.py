from django.test import TestCase

from blog.models import Post, Comment


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="first post", content="content of the first post")

    def tearDown(self):
        pass

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.title}"
        self.assertEqual(expected_object_name, "first post")

    def test_content_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.content}"
        self.assertEqual(expected_object_name, "content of the first post")


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Comment.objects.create(
            post=Post.objects.create(title="first post", content="content of the first post"),
            name="first comment",
            email="test@example.com",
            password="testpassword",
            message="message of the first comment",
        )

    def tearDown(self):
        pass

    def test_name_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f"{comment.name}"
        self.assertEqual(expected_object_name, "first comment")

    def test_email_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f"{comment.email}"
        self.assertEqual(expected_object_name, "test@example.com")

    def test_password_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f"{comment.password}"
        self.assertEqual(expected_object_name, "testpassword")

    def test_message_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f"{comment.message}"
        self.assertEqual(expected_object_name, "message of the first comment")

    def test_post_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f"{comment.post}"
        self.assertEqual(expected_object_name, "first post")

    def test_post_related_name(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.comments.all()[0]}"
        self.assertEqual(expected_object_name, "first comment")
