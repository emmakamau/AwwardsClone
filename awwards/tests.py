from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class TestUser(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.example_user, User))

class TestProfile(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma",phone="+254700123123",fax_number="+254700123123",
        linkedin="https://emmak")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.example_profile, Profile))

class TestProject(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma",phone="+254700123123",fax_number="+254700123123",
        linkedin="https://emmak")
        self.example_profile.save()

        self.example_project = Project(owner=self.example_profile,title="project one",description="Lorem ipsum",
        project_image="../assets/avatar.png",project_url="https://project_one")

    def tearDown(self) -> None:
        Project.objects.all().delete()
        Project.objects.all().delete()

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.example_project, Project))

    def test_del_instance(self):
        self.example_project.save()
        self.example_project.delete()
        self.assertTrue(len(Project.objects.all()) == 0)

class TestDesignVote(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()
        
        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_project = Project(owner=self.example_profile,title="project one",description="Lorem ipsum",
        project_image="../assets/avatar.png",project_url="https://project_one")

        self.example_design_vote = DesignVote(profile_vote=self.example_profile,post_voted=self.example_project)

    def test_instance_design_vote(self):
        self.assertTrue(isinstance(self.example_design_vote, DesignVote))

class TestUsabilityVote(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()
        
        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_project = Project(owner=self.example_profile,title="project one",description="Lorem ipsum",
        project_image="../assets/avatar.png",project_url="https://project_one")

        self.example_usability_vote = UsabilityVote(profile_vote=self.example_profile,post_voted=self.example_project)

    def test_instance_usability_vote(self):
        self.assertTrue(isinstance(self.example_usability_vote, UsabilityVote))


class TestContentVote(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()
        
        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_project = Project(owner=self.example_profile,title="project one",description="Lorem ipsum",
        project_image="../assets/avatar.png",project_url="https://project_one")

        self.example_content_vote = ContentVote(profile_vote=self.example_profile,post_voted=self.example_project)

    def test_instance_content_vote(self):
        self.assertTrue(isinstance(self.example_content_vote, ContentVote))