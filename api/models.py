from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone 
import uuid 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission

class WORKER_TYPE(models.IntegerChoices):
    IT = 2, 'IT'
    WORKER = 5, 'Worker'
    CLEANER = 6, 'Cleaner'
    OTHER = 7, 'Other'

class USER_TYPE(models.IntegerChoices):
    ADMIN = 1, 'Admin'
    USER = 2, 'User'
    WORKER = 3, 'Worker'

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False) 
    is_deleted = models.BooleanField(default=False) 

    class Meta:
        abstract = True
        ordering = ['created']

class UserManager(BaseUserManager):
    """Manager for User Profile"""

    def create_user(self, first_name, last_name, email, phone, role, password=None, **extra_fields):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            role=role,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=25, unique=True, blank=True) 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    role = models.IntegerField(choices=USER_TYPE.choices, default=USER_TYPE.USER, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(Group, related_name='api_users')
    user_permissions = models.ManyToManyField(Permission, related_name='api_users')

    objects = UserManager()

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.phone if self.phone else self.email

class Worker(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    worker_type = models.IntegerField(choices=WORKER_TYPE.choices, default=WORKER_TYPE.WORKER, db_index=True)
    is_busy = models.BooleanField(default=False, db_index=True)
    def __str__(self):
        return f'{self.user}: {self.worker_type}'

class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True) 
    phone = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return f'{self.name}'


class Building(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, db_index=True)
    name = models.CharField(max_length=255, blank=True)
    floor_count = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.name or "Building"

class Office(BaseModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, db_index=True)
    floor = models.IntegerField(default=0, db_index=True)
    number = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.building} | {self.number}'

class UserOffice(BaseModel):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.office}: {self.user}'
