from pydoc import describe
from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    #blank as false = required field
    #null means if the database can be empty or not
    title = models.CharField(max_length=120) #maxlength is required
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank = False, null = False)
    featured = models.BooleanField(default = False) # null = True, default = True

    def get_absolute_url(self):
        #return f"/product/{self.id}/" #works fine, but hardcoded
        return reverse("products:product-detail", kwargs={"id": self.id}) #but this is how django prefers it
    