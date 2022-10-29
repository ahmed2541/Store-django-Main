from datetime import datetime
from email.policy import default
from sqlite3 import Date
from turtle import mode
from winreg import ConnectRegistry
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name ='signup',on_delete=models.CASCADE,verbose_name=_('user'))
    country = CountryField()
    location = models.CharField(max_length=100,default='',verbose_name=_('Location'))
    phone_number = models.CharField(max_length=15,verbose_name=_('Phone Number'))
    image = models.ImageField(upload_to='Images_profiles/%y/%m/%d',blank=True,null=True,verbose_name=_('Image'))
    join_date = models.DateTimeField(default=datetime.now,verbose_name=_('Date'))
    slug = models.SlugField(blank=True,null=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.user)

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.user, allow_unicode=True)
    #     super(Profile,self).save(*args,**kwargs)

    # def get_absolute_url(self):
    #     return reverse("profile:edit_profile", kwargs={"slug": self.slug})



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class ProfileEdit(models.Model):
    profile = models.OneToOneField(Profile,related_name ='edit_profile',on_delete=models.CASCADE,verbose_name=_('Profile'))
    image = models.ImageField(upload_to='Images_profiles/%y/%m/%d',blank=True,null=True,verbose_name=_('Image'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = CountryField()
    location = models.CharField(max_length=100,default='',verbose_name=_('Location'))
    phone_number = models.CharField(max_length=15,verbose_name=_('Phone Number'))

