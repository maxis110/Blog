from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comments
from django.shortcuts import get_object_or_404

# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        self.user = get_user_model()

    def test_user_create_success(self):
        self.user.objects._create_user(username='TEST', email='TEST@test.com', password='123456Test')
        self.assertEqual(self.user.objects.all().count(), 1)
        self.assertEqual(self.user.objects.all()[0].username, 'TEST')
        self.assertEqual(self.user.objects.all()[0].email, 'TEST@test.com')
        self.assertEqual(self.user.objects.all()[0].check_password('123456Test'), True)

    def test_user_delete_success(self):
        pass

class PostTest(TestCase):

    def setUp(self):
        self.dummy = Post.objects.create(title='dummy')
        self.form = Post.objects

    def test_post_create_success(self):
        self.new_dummy = self.form.create(title='test')
        self.new_dummy.save()
        self.assertEqual(self.new_dummy.title, 'test')

    def test_post_edit_success(self):
        self.assertEquals(self.dummy.title, 'dummy')
        self.dummy.title='new_title'
        self.dummy.save()
        self.assertEquals(self.dummy.title, 'new_title')

    def test_post_delete_success(self):
        test = Post.objects.create(title='dummy')
        test.save()
        test_id = test.id
        self.assertEquals(len(self.form.filter(id=test_id)), 1)
        test.delete()
        self.assertEquals(len(self.form.filter(id=test_id)), 0)

class CommentsTest(TestCase):

    def setUp(self):
        self.comment = Comments.objects

    def test_comment_create_success(self):
        new_post = Post.objects.create(title='dummy')
        new_post.save()
        new_user = get_user_model().objects._create_user(username='TEST', email='TEST@test.com', password='123456Test')
        self.new_comment = self.comment.create(comments_text='test', autors_id=1, comments_post_id=1)
        self.new_comment.save()
        self.assertEqual(self.new_comment.comments_text, 'test')


    def test_comment_delete_success(self):
        new_post = Post.objects.create(title='dummy')
        new_post.save()
        new_user = get_user_model().objects._create_user(username='TEST', email='TEST@test.com', password='123456Test')
        self.new_comment = self.comment.create(comments_text='test', autors_id=2, comments_post_id=2)
        self.new_comment.save()
        self.assertEqual(self.comment.all().count(), 1)
        self.new_comment.delete()
        self.assertEqual(self.comment.all().count(), 0)