from django.db import models
from django.contrib.auth import get_user_model



# TODO fix me
class Listing(models.Model):
    title = models.Charfield(max_lenght=256)
    address = models.Charfield(max_lenght=256)
    
    realtor = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="listings")
    desc= models.TextField(blank=True)
    
    price = models.DecimalField(max_digit=12, decimal_places=1)
    bed_rooms= models.IntegerField()
    bathroom = models.DecimalField(decimal_places=2, max_digits=5)
    garage = models.BooleanField(default=False)
    sqft = models.DecimalField(decimal_places=3, max_digits=12)
    is_pub= models.BooleanField()
    created_at = models.DateField(auto_now=True)
    


class ListingImages(models.Model):
    file = models.ImageField(upload_to="/listing/")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="images")



class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="contacts")
    # TODO add relate if needed
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # FIXME add soft delete
    created_at = models.DateField(auto_now=True)