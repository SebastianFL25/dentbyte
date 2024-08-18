from django.db import models
from users.models import CustomUser

class Company(models.Model):
    identification = models.CharField(max_length=50, unique=True) 
    legal_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.legal_name

class CompanyMembership(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role
    
class Clients(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    identification_type = models.CharField(max_length=50)
    personal_identification = models.CharField(max_length=100)

    def __str__(self):
        return f"Cliente Creado {self.name} {self.personal_identification}"