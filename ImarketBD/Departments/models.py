from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# User Register models.

class userManager(BaseUserManager):
    def create_user(self,email,username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user    = self.create_user(
            email=self.normalize_email(email),
            password= password,
            username=username,
        )

        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.save(using=self._db)
        return user


organizations_Choices=[
        ('Ministry of Commerce','Commerce'),
        ('Ministry of Agriculture','Agriculture'),
        ('Bangladesh Bank','Bank'),
        ('Port Authority','Custom'),
    ]


class userInformation(AbstractBaseUser):
    first_name                          =models.CharField(max_length=30)
    last_name                           =models.CharField(max_length=30)
    phone_number                        =models.CharField(max_length=30)
    nationality                         =models.CharField(max_length=30)
    national_id_number                  =models.CharField(max_length=30)
    address                             =models.CharField(max_length=250)

    organizations                       =models.CharField(max_length=30,choices=organizations_Choices)
    organizational_role                 =models.CharField(max_length=30)
    reference_email                     =models.EmailField(verbose_name="reference_email",max_length=60)
    describtion                         =models.TextField(max_length=250)

    username                            =models.CharField(max_length=30, unique=True)
    email                               =models.EmailField(verbose_name="email",max_length=60, unique=True)

    date_joined                         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login                          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                            = models.BooleanField(default=False)
    is_active                           = models.BooleanField(default=True)
    is_staff                            = models.BooleanField(default=False)
    is_superuser                        = models.BooleanField(default=False)
    is_webadmin                         = models.BooleanField(default=False)
    is_allow                            = models.BooleanField(default=False)
    is_commerce                         = models.BooleanField(default=False)
    is_agriculture                      = models.BooleanField(default=False)
    is_bank                             = models.BooleanField(default=False)
    is_custom                           = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username'] 

    objects =userManager()

    def __str__(self):
        return self.email + "," + self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
