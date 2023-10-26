from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)
    image = models.FileField()
    description = models.TextField(null=True, blank=True)
    follower = models.ManyToManyField('self', symmetrical=False, blank=True)


    def __str__(self):
        return self.name

    def update_image(self, file):
        self.image.storage.delete(self.image.name)
        self.image = file


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def image_url(self):
        return f'/static/images/{self.name}.jpg'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text
