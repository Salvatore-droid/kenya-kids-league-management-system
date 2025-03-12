from django.db import models
from django.contrib.auth.models import User


class Campus(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HighSchool(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ManageCourse(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CampusLeveling(models.Model):
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HighschoolLeveling(models.Model):
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MiddleschoolLeveling(models.Model):
    name = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Candidate Model
class CampusStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True)
    course = models.ForeignKey(ManageCourse, on_delete=models.SET_NULL, null=True, blank=False)
    school = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, blank=True)  # Add school field

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class HighschoolStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True)
    level = models.ForeignKey(HighschoolLeveling, on_delete=models.SET_NULL, null=True, blank=False)
    school = models.ForeignKey(HighSchool, on_delete=models.SET_NULL, null=True, blank=True)  # Add school field


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class MiddleschoolStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True)
    grade = models.ForeignKey(MiddleschoolLeveling, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url






class CampusStudentResult(models.Model):
    campus = models.ForeignKey(CampusStudent, on_delete=models.CASCADE)
    test = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HighschoolStudentResult(models.Model):
    high = models.ForeignKey(HighschoolStudent, on_delete=models.CASCADE)
    test = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





