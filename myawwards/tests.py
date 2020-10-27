from django.test import TestCase
from .models import *

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='milly', password='qwerty123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestRates(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='milly')
        self.rate= Rates(design=1, usability=1, content=1, project=1, user= self.user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rates))

    def test_save_rate(self):
        self.rate.save_rate()
        rates= Rates.objects.all()
        self.assertTrue(len(rates) > 0)

class TestProjects (TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='milly')
        self.project= Projects(design=1, usability=1, content=1,  user= self.user, name= 'Gallery', description= 'app that displaysimages', image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e',
        link='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Projects))

    def test_search_project(self):
        self.project.save()
        project = Projects.search_project('test')
        self.assertTrue(len(project) > 0)
