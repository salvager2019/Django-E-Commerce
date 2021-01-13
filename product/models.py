from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Category(models.Model):
    STATUS=(('True','True'),('False','False'))

    parent=models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    img=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (('True', 'True'), ('False', 'False'))

    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to on relation with Category
    title = models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    price =models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    detail=models.TextField()
    slug = models.SlugField()
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    ##method to create a fake table field in read only model. this is add github
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    image_tag.short_description="Image"


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
