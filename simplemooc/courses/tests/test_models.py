from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from model_mommy import mommy

from simplemooc.courses.models import Course

class CourseManagerTestCase(TestCase):

    def setUp(self):
        self.courses = mommy.make('courses.Course', name='Python na Web com Django', _quantity=3)
        self.courses = mommy.make('courses.Course', name='Python para Devs', _quantity=10)
        self.client = Client()

    def tearDown(self):
        Course.objects.all().delete()

    def test_course_search(self):
        search = Course.objects.search('django')
        self.assertEqual(len(search), 3)
        search = Course.objects.search('devs')
        self.assertEqual(len(search), 10)
        search = Course.objects.search('python')
        self.assertEqual(len(search), 13)