from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None,):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    address_line2 = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)
    zip_code = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    month = models.CharField(blank=True, max_length=255)
    day = models.CharField(blank=True, max_length=255)
    year = models.CharField(blank=True, max_length=255)
    security_number1 = models.CharField(blank=True, max_length=255)
    security_number2 = models.CharField(blank=True, max_length=255)
    security_number3 = models.CharField(blank=True, max_length=255)
    citizenship = models.CharField(blank=True, max_length=255)
    marital_status = models.CharField(blank=True, max_length=255)
    no_of_dependents = models.CharField(blank=True, max_length=255)
    investment_experience = models.CharField(blank=True, max_length=255)
    employment_status = models.CharField(blank=True, max_length=255)
    employee_name = models.CharField(blank=True, max_length=255)
    occupation = models.CharField(blank=True, max_length=255)
    trade_options = models.CharField(blank=True, max_length=255)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin