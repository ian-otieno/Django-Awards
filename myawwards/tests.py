from django.test import TestCase
from .models import UserProfile, Project, Rating, User
# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'iano', password ='iano2345')
        self.user.save()
        self.iano= UserProfile(profile_photo='2020-audi-a4-facelift-sketch.jpg', bio = 'okay', phone_number = 783327162, user = self.user)
        self.iano.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.iano, UserProfile))

    def test_save_method(self):
        self.iano.save_profile()
        profile = UserProfile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.iano.save_profile()
        profile = UserProfile.objects.all()
        self.iano.delete_profile()
        self.assertTrue(len(profile)==0)

class TestProject(TestCase):
    def setUP(self):
        self.iano = UserProfile(profile_photo='2020-audi-a4-facelift-sketch.jpg', bio = 'software developer',phone_number = 717878813, user = User(username = 'iano', password ='iano2345'))
        self.iano.save_profile()

        self.new_project = Project(project_title = 'News-App', project_image='JPEG image', project_description='okay', project_link='https://ianonewsapp.herokuapp.com/', user = self.iano)
        self.new_project.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))


    def test_save_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.new_project.delete_project()
        self.assertTrue(len(projects)==0)

class TestRating(TestCase):
    def setUp(self):
        self.iano = UserProfile(profile_photo='2020-audi-a4-facelift-sketch.jpg', bio = 'software developer',phone_number = 783327162, user = User(username = 'iano', password ='iano2345'))
        self.iano.save_profile()

        self.new_project = Project(project_title = 'News-App', project_image='JPEG image', project_description='software developer', project_link='https://ianonewsapp.herokuapp.com/', user = self.iano)
        self.new_project.save()

        self.rating = Rating(design=2, usability=3, content=4, user = self.iano, project=self.new_project)
        self.rating.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_method(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating)>0)