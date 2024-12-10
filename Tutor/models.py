from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Course Title")
    description = models.TextField(verbose_name="Course Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Course Price")
    seats_available = models.IntegerField(default=0, verbose_name="Available Seats")

    def __str__(self):
        return self.title

class Checkout(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # ForeignKey relationship
    payment_method = models.CharField(max_length=50)
    mpesa_number = models.CharField(max_length=20, default=1)

    def __str__(self):
        return f"{self.name} - {self.course.title}"



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
class  Member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name