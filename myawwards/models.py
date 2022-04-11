from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_photo = CloudinaryField('profile')
    bio = models.TextField(default='')
    phone_number = models.IntegerField(default=717878813)

    
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Project(models.Model):
    project_title = models.CharField(max_length= 30)
    project_image = CloudinaryField('images')
    project_description = models.TextField()
    project_link = models.URLField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        return cls.objects.filter(project_title__icontains=search_term).all()

class Rating(models.Model):
    design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.project} Rating' 

    def save_rating(self):
        self.save()