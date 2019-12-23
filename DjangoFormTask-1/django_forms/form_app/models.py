from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=127)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return f'{self.name}'


class CustomModel(models.Model):
    state = models.ForeignKey(State,related_name='states',on_delete=models.CASCADE)
    email = models.EmailField('Email',max_length=63)
    password = models.CharField('Password',max_length = 63)
    address1 = models.CharField('Address1',max_length=255)
    address2 = models.CharField('Address2',max_length=255)
    city = models.CharField('City',max_length=63)
    zip = models.CharField('Zip code',max_length = 20)
    check = models.BooleanField('Check',default=False)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return f'{self.email} {self.city}'
