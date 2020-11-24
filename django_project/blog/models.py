from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    MEMBER_CHOICES = [
        ('No one', 'No One'),
        ('Alex Lianardo', 'Alex Lianardo'),
        ('Muhammad Ikhwan Khalid', 'Muhammad Ikhwan Khalid'),
    ]
    member = models.CharField(
        max_length= 100,
        choices=MEMBER_CHOICES,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
