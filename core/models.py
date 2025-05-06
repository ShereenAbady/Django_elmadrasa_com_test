from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')
    charged_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)  
    currency = models.CharField(max_length=10, default='usd')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.title

