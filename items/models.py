from django.db import models

# Create your models here.
class ItemDetails(models.Model):
    location = [
        ("ALL", "All"),
        ("CANTEEN", "Canteen"),
        ("GYM", "Gym"),
        ("HS_GROUNDS", "Highschool Grounds"),
        ("BASEMENT", "Basement"),
        ("MAIN_BLDG", "Main Building"),
        ("SAO_LOBBY", "Sao Lobby"),
        ("PARKING_AREA", "Parking Area"),
    ]

    category = [
        ("ALL", "All"),
        ("PERSONAL", "Personal"),
        ("ACCESSORIES", "Accessories"),
        ("ID", "Id"),
        ("ELECTRONICS", "Electronics"),
        ("KEYS", "Keys"),
        ("VALUABLES", "Valuables"),
    ]

    status = [
        ("LOST", "Lost"),
        ("FOUND", "Found"),
    ]
    item_name = models.CharField(max_length=30)
    item_category = models.CharField(choices=category, default="ALL", max_length=30)
    item_location = models.CharField(choices=location, default="ALL", max_length=30)
    item_date_and_time = models.DateTimeField(max_length=15)
    item_image = models.ImageField(upload_to='items_photos/', null=True, blank=True)
    item_status = models.CharField(choices=status, max_length=5)

    def __str__(self):
        return self.item_name