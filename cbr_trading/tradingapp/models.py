
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
COLOR_CHOICES = (
    ('Consumer','Consumer'),
    ('Provider','Provider'),
)

class t_user(models.Model):
    user_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=200, unique=True)
    secret = models.CharField(max_length=200)
    email = models.EmailField(_('email'), unique=True)
    #User._meta.get_field('email')._unique = True
    full_name = models.CharField(max_length=200)
    nic = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=COLOR_CHOICES, default='Consumer')
    verified = models.CharField(max_length=200)
    creation_date = models.DateField()
    modification_date = models.DateField()




class t_products(models.Model):
    product_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    enabled = models.CharField(max_length=10)
    creation_date = models.DateField()
    modification_date = models.DateField()

class t_product_provider(models.Model):
    t_product_provider_id = models.IntegerField(primary_key=True)
    enabled = models.CharField(max_length=10)
    rating = models.IntegerField(200)
    location = models.CharField(max_length=100)
    volunteer = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    long = models.IntegerField()
    width = models.IntegerField()
    creation_date = models.DateField()
    modification_date = models.DateField()

    user_id = models.ForeignKey(t_user,related_name='user', on_delete=models.PROTECT )
    product_id = models.ForeignKey(t_products,related_name='products', on_delete=models.CASCADE)

class t_announcements(models.Model):
    id =  models.IntegerField(primary_key=True)
    content = models.CharField(max_length=400)
    creation_date = models.DateField()
    modification_date = models.DateField()

    t_product_provider_id = models.ForeignKey(t_product_provider,related_name='productrovider2', on_delete=models.CASCADE)

class t_consumptions(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    status = models.CharField(max_length=100)
    enabled = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    creation_date = models.DateField()
    modification_date = models.DateField()
    t_product_provider_id = models.ForeignKey(t_product_provider, related_name='productrovider1',
                                              on_delete=models.CASCADE)
    user_id = models.ForeignKey(t_user, related_name='user1', on_delete=models.PROTECT)















