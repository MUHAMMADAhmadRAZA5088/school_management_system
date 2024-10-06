from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Student(models.Model):
    CLASS_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]
    
    SECTION_CHOICES = [
        ('Abu Baker', 'Abu Baker'),
        ('Umer', 'Umer'),
        ('Usman', 'Usman'),
        ('Ali', 'Ali'),
    ]

    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    b_form_id = models.CharField(max_length=20)
    father_id_card = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    student_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    dob = models.DateField()
    picture = models.ImageField(upload_to='student_pictures/', null=True, blank=True)
    address = models.TextField()
    start_date = models.DateField(auto_now_add=True, null=True)
    registration_number = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.student_name


@receiver(pre_save, sender=Student)
def generate_registration_number(sender, instance, **kwargs):
    if not instance.registration_number:  # Agar registration_number pehle se nahi hai
        last_student = Student.objects.all().order_by('id').last()
        if last_student:
            last_id = int(last_student.registration_number[5:])  # "JMI1k" ko chhod kar number extract karna
            new_id = last_id + 1
        else:
            new_id = 1  # Agar pehla student hai, toh ID 1 se start ho
        instance.registration_number = f"JMI10{new_id}"  

class Class(models.Model):
    class_name = models.CharField(max_length=100)  

class Section(models.Model):
    section = models.CharField(max_length=100)
