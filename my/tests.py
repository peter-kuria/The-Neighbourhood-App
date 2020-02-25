from django.test import TestCase

# Create your tests here.
from .models import *



class ProfileTestClass(TestCase):
    #Set up method

    def setUp(self):

        self.new_profile = Profile(user_id=2,hood_id=3,bio="just testing", email='titusouko@gmail.com',name="Titus",profile_pic="image.jpeg")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def tearDown(self):
        Profile.objects.all().delete()
