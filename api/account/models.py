from django.db import models
from account.managers import AccountManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    is_active = models.BooleanField(_('active'), default=True)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    mobile_number = models.CharField(max_length=13)
    date_of_birth = models.DateTimeField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=25)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AccountManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'