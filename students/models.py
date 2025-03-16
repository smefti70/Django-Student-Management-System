from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
         ("Full Stack Web Development with Python and Django", "Full Stack Web Development with Python and Django"),
        ("Machine Learning", "Machine Learning"),
        ("Data Science", "Data Science"),
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Cyber Security", "Cyber Security"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return self.name
