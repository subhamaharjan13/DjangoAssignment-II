from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    profile_photo = models.ImageField(upload_to='static/images/profile_pics',
                                      default='static/images/nophoto.png')

    def __str__(self):
        return self.username


class Image(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profile_pics',
                              default='nophoto.png')
