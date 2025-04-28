from django.db import models

# Create your models here.


#lab11 



class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')



class Student2(models.Model):
    name = models.CharField(max_length=100)
    addresses = models.ManyToManyField('Address2')

class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=100) 

class Card(models.Model):
    card_number = models.IntegerField()

class Address(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    #address = models.OneToOneField(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
