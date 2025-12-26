from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

class shopping(models.Model):
    TYPE_OF_PRODUCT_COLORS  = [
        ('RD', 'RED'),
        ('WH', 'WHITE'),
        ('GRN', 'GREEN'),
        ('BL', 'BLUE'),
    ]
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to="product_images/")
    product_description = models.TextField()
    product_colors = models.CharField(max_length=3,choices=TYPE_OF_PRODUCT_COLORS)

    def __str__(self):
        return self.product_name
