from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        unique_together = ('name', 'parent',)    #enforcing that there can not be two

    """ def __str__(self):
        return self.name """
    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    size = models.CharField(max_length=10, null=True)
    stock = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='img/')
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_cat_list(self):           #for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

class ProductPicture(models.Model):
    caption = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/')
    added_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
