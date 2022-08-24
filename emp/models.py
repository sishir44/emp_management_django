from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=10)

    # to show the name in place of Empobject
    def __str__(self):
        return self.name


# create Testimonal App 
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField(max_length=1)

    # to override
    def __str__(self):
        return self.testimonial