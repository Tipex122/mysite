from django.db import models

# Create your models here.
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    budget = models.FloatField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

####################################################################################
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name="Estimated budget", blank=True, null=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = u"Categories"

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    category = TreeForeignKey('Category', null=True, blank=True, db_index=True)
#    image = models.ImageField(upload_to='foto', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stocks = models.IntegerField(default=0, blank=True)

    #PRICES
    priceAustria = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name="Recomended Price", blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def image_img(self):
        if self.image:
            return u'<img src="%s" width="75" height="75" />' % (self.image.url)
        else:
            return '(No image)'
    image_img.short_description = 'Image'
    image_img.allow_tags = True
