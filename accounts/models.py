from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *
from django.utils import timezone
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    phoneNumber = models.CharField(unique=True, max_length=11)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
    Avatar = models.ImageField(upload_to="images/Avatar",blank=True,null=True)
    is_author = models.BooleanField(default = False, verbose_name = "وضعیت نویسندگی")

    code = models.IntegerField(blank=True,null=True)


    USERNAME_FIELD = 'phoneNumber'
    objects = MyUserManager()

    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    def name(self):
        return str(self.firstName) + " " + str(self.lastName)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر ویژه"
