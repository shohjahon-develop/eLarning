from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Add(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')



    def __str__(self):
        return self.name

class Bot(models.Model):
    class Status(models.TextChoices):
        Yaroqli = "YR","Yaroqli"
        Yaroqsiz = "YS","Yaroqsiz"
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=300)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("botsDetail", args=[self.slug])





class Web(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')


    def __str__(self):
        return self.name

class Papular(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    number = models.IntegerField()
    time = models.FloatField()
    tname = models.CharField(max_length=300)
    snumber = models.TextField()

    def __str__(self):
        return self.name


class Expert(models.Model):
    name = models.CharField(max_length=300)
    subject = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name




class Exp(models.Model):
    name = models.CharField(max_length=300)
    job = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Aexp(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/img')

    def __str__(self):
        return self.name


class Instruct(models.Model):
    name = models.CharField(max_length=400)
    bio = models.TextField()
    img = models.ImageField(upload_to='courses/img')

    def __str__(self):
        return self.name


class Cour(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to="courses/img")
    price = models.IntegerField()
    time = models.FloatField()
    std = models.TextField()
    nub = models.IntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=400)
    bio = models.TextField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='team/img')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __dir__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=300)
    cost = models.IntegerField()
    slug = models.SlugField(max_length=300)
    tutor = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    numPupils = models.IntegerField()
    number = models.IntegerField()
    img = models.ImageField(upload_to='index/img')



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("coursedetail", args=[self.slug])











































































































































































































































































