from django.db import models

class registeringo(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.username


class addhouse(models.Model):
    location = models.CharField(max_length=15)
    sq_feet = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    rupees = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    cover = models.ImageField(upload_to='add_house/img/', null=True, blank=True)

    def __str__(self):
        return self.location




    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.







