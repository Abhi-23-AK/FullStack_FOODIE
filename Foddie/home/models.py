from django.db import models

class ReachOut(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.username


from django.db import models

class Variety(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='varieties/')  # stores image path

    def __str__(self):
        return self.name
