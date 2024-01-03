from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    email = models.EmailField(max_length=300, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    house_no = models.CharField(max_length=50, null=True, blank=True)          # could be name
    street = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_subscriber = models.BooleanField(default=False)
    is_newsletter = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False) # ask for? if so include option to not specify
    deleted_at = models.DateTimeField(null=True, blank=True)  # can be used to prema-delete users after 30 days and allow account restoration, or delete all user details except id so orders data table isn't broke, and orders can stillm be linked to a user id
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = []      
    objects = UserManager()
    

    # handle errors when too many characters submitted

    # use library like like django-phonenumber-field or django-localflavor for phone number validation

    # User subscription: If users can subscribe to multiple products, you may need a ManyToManyField to a Product model to keep track of these subscriptions.

    # Newsletter subscription date: If you want to know when the user subscribed to the newsletter, you might add a DateTimeField for it.

    # Saved articles: If users can save articles, you may need a ManyToManyField to an Article model, assuming you have a separate Article model.

    # Billing Info: If users can make purchases, you may need to store their billing information. This could include a BillingInfo model with fields for credit card info, billing address, etc. However, note that storing credit card information has major security implications and often it's best to use a third-party payment processor that handles all of this for you.

    # Order History: You might want an Order model to store each user's past orders. Each Order could then have a ForeignKey to the User, creating a many-to-one relationship from orders to users