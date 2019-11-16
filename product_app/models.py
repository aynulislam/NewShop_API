from django.db import models

class SpCategory(models.Model):
    category = models.CharField(max_length=1000)
    colours = models.CharField(max_length=1000,null=True)
    size = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.category


class SpSubCategory(models.Model):
    category_id = models.ForeignKey(SpCategory, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.category_id)

class SpDivision(models.Model):
    division = models.CharField(max_length=20)
    minimum_qty = models.IntegerField()

    def __str__(self):
        return self.division

class SpProduct(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=100, null=False)
    division_id = models.ForeignKey(SpDivision, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SpSubCategory, on_delete=models.CASCADE)
    description = models.TextField(max_length=100000,null=True)
    password = models.CharField(max_length=255,null=True)
    minimum_qty = models.IntegerField()
    date = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_code)

