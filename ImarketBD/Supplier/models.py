from django.db import models
from django.utils import timezone
from Commodities.models import commodities_info
from Departments.models import userInformation

# Bangladesh bank LC opening and settelment models here.
Product_Choices=[
        ('Rice','Rice'),
        ('Wheat','Wheat'),
        ('Onion','Onion'),
        ('Garlic','Garlic'),
        ('Egg','Egg'),
        ('Potato','Potato'),
        ('Ginger','Ginger'),
        ('Maize','Maize'),
        ('Dry Chili','Dry Chili'),
        ('Termaric','Termaric'),
        ('Dates','Dates'),
        ('Milk Powder','Milk Powder'),
        ('Baby Food','Baby Food'),
        ('Cumin (Zira)','Cumin (Zira)'),
        ('Cardamom (Elachi)','Cardamom (Elachi)'),
        ('Cinnamon (Daruchini)','Cinnamon (Daruchini)'),
        ('Black Pepper (Gol marich)','Black Pepper (Gol marich)'),
        ('Cloves (Labanga)','Cloves (Labanga)'),
        ('Coriander (Dhania)','Coriander (Dhania'),
        ('Yellow Peas','Yellow Peas'),
        ('Cassia leaf (Tezpata)','Cassia leaf (Tezpata)'),
        ('Chola(Seed/Asto)','Chola(Seed/Asto)'),
        ('Cheak Peas','Cheak Peas'),
        ('Raw Salt','Raw Salt'),
        ('Refined Salt','Refined Salt'),
        ('Raw Sugar','Raw Sugar'),
        ('Refined Sugar','Refined Sugar'),
        ('Crude Soyabean','Crude Soyabean'),
        ('Refined Soyabean','Refined Soyabean'),
        ('Seed Soyabean','Seed Soyabean'),
        ('Crude palm Oil','Crude palm Oil'),
        ('Refined palm Oil','Refined palm Oil'),
        ('Seed palm Oil','Seed palm Oil'),
        ('Masur Dal','Masur Dal'),
        ('Chola Dal','Chola Dal'),
        ('Ankor Dal','Ankor Dal'),
        ('Mugh Dal','Mugh Dal'),
        ('Other Pulses','Other Pulses'),
    ]

class lc_information(models.Model):
    lc_ID                           =models.CharField(max_length=50, unique=True)
    commodities_ID                  =models.ForeignKey(
        commodities_info, 
        on_delete=models.CASCADE,
        default=None
     ) 
    product_Name                    =models.CharField(max_length=100,choices=Product_Choices)
    opening_quantity                =models.CharField(max_length=100)
    opening_value_cost              =models.CharField(max_length=100)
    opening_date                    =models.CharField(max_length=100)
    settled_quantity                =models.CharField(max_length=100)
    settled_value_cost              =models.CharField(max_length=100)
    settled_date                    =models.CharField(max_length=100)
    lc_importer_name                =models.CharField(max_length=100)
    importer_phone_number           =models.CharField(max_length=100, unique=True)
    opening_bank_name               =models.CharField(max_length=100)
    bank_account_number             =models.CharField(max_length=100, unique=True)
    email                                  =models.ForeignKey(
        userInformation, 
        on_delete=models.CASCADE,
        default=None
     )

    insertion_time                  =models.DateField(auto_now=True, auto_now_add=False)
    last_updated                    =models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.product_Name

    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        elif not self.last_updated is not None:
            self.last_updated = None
        super(lc_information, self).save(*args, **kwargs)

class importer_information(models.Model):
    importer_ID                     =models.CharField(max_length=50, unique=True)
    importer_name                   =models.CharField(max_length=50)
    importer_Nid                    =models.CharField(max_length=50, unique=True)
    importer_phone_number           =models.CharField(max_length=50, unique=True)
    importer_photo                  =models.ImageField(upload_to='photo')
    bank_name                       =models.CharField(max_length=100)
    bank_account_number             =models.CharField(max_length=100, unique=True)
    insertion_time                  =models.DateTimeField(auto_now=True, auto_now_add=False)
    last_updated                    =models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.importer_name + "," + self.importer_ID

    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        elif not self.last_updated is not None:
            self.last_updated = None
        super(importer_information, self).save(*args, **kwargs)