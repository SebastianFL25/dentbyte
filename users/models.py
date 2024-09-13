from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,UserManager
from django.contrib.auth.hashers import make_password
from django.apps import apps

class CustomManagerUser(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_admin", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")

        return self._create_user(username, email, password, **extra_fields)

#     def create_user(self,username,email,password,first_name,last_name= None):

#         if not email:
#             raise ValueError('Usuario necesita email')
        
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#             password = password,
#             first_name =first_name,
#             last_name = last_name
#         )

#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self,username,email,password):

#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#             password = password
#         )

#         user.set_password(password)
#         user.is_admin = True
#         user.save()
#         return user
 
class CustomUser(AbstractBaseUser):

    username = models.CharField('Name of User', unique=True, max_length=100)
    email = models.EmailField('Email adress', unique= True, max_length=100, default='example@email.com')
    first_name = models.CharField('Name', unique=True, max_length=100, blank= True, null= True)
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
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


