from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class CustomManagerUser(BaseUserManager):

    def create_user(self,username,email,password= None):

        if not email:
            raise ValueError('Usuario necesita email')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            password = password
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,password):

        user = self.create_user(
            username = username,
            email = email,
            password = password
        )

        user.is_admin = True
        user.save()
        return user
 
class CustomUser(AbstractBaseUser):

    username = models.CharField('Name of User', unique=True, max_length=100)
    email = models.EmailField('Email adress', unique= True, max_length=100, default='example@email.com')
    name = models.CharField('Name', unique=True, max_length=100, blank= True, null= True)
    last_name = models.CharField('Last Name', unique=True, max_length=100, blank= True, null= True)
    phone_number = models.CharField('Phone Number', unique=True, max_length=100, blank= True, null= True)
    image = models.ImageField('Profile Picture',upload_to='profile/',height_field=None, width_field=None, max_length=200, default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomManagerUser()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return f'{self.username} {self.last_name}'
    
    def has_perms(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


