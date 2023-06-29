from django.db import models
from django.contrib.auth.models import User

# CREATE MODEL FOR FLAT OWNER
class FlatOwner(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE) 
    mobile = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username 


# CREATE MODE FOR ADD FLAT
class AddFlat(models.Model):
    owner = models.ForeignKey(FlatOwner, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=20)
    price = models.IntegerField()
    flat_type = models.CharField(max_length=30, null=True)
    image = models.FileField(upload_to="media", null=True)
    city = models.CharField(max_length=200, null=True)
    desc = models.TextField()
    flatstatus = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.address
    

# CREATE MODEL FOR USER
class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username
    

# CREATE MODEL FOR CONTACT US
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name