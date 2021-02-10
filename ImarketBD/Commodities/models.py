from django.db import models
from Departments.models import userInformation
from django.utils import timezone

# All Commodities models.


#Over_All Commodities Information.

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
#Commodities Informations
class commodities_info(models.Model):

    commodities_ID              =models.CharField(max_length=50, unique=True)
    production_Code             =models.CharField(max_length=50, unique=True, null=True)
    import_Code                 =models.CharField(max_length=50, unique=True, null=True)
    product_Name                =models.CharField(max_length=80,choices=Product_Choices)

    market_demand               =models.DecimalField(max_digits=9, decimal_places=2, null=True)
    market_consumption          =models.DecimalField(max_digits=9, decimal_places=2, null=True)
    current_stroage             =models.DecimalField(max_digits=9, decimal_places=2, null=True)

    unit_price                  =models.IntegerField()
    wholeseller_price           =models.IntegerField()
    supplier_price              =models.IntegerField()
    international_price         =models.IntegerField()
    email                                  =models.ForeignKey(
        userInformation, 
        on_delete=models.CASCADE,
        default=None
     )

    production_cost             =models.DecimalField(max_digits=9, decimal_places=2, null=True)
    import_cost                 =models.DecimalField(max_digits=9, decimal_places=2, null=True)
    transport_cost              =models.DecimalField(max_digits=9, decimal_places=2, null=True)

    insertion_time              =models.DateTimeField(auto_now=True, auto_now_add=False)
    last_updated                =models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.product_Name + "," + self.commodities_ID
    
    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        elif not self.last_updated is not None:
            self.last_updated = None
        super(commodities_info, self).save(*args, **kwargs)



#Production Table
class commodities_production(models.Model):
    
    product_Name                           =models.CharField(max_length=80,choices=Product_Choices)
    production_quantity                    =models.DecimalField(max_digits=9, decimal_places=2)
    production_cost                        =models.DecimalField(max_digits=9, decimal_places=2)
    production_place                       =models.CharField(max_length=150)
    production_date                        =models.CharField(max_length=30)
    email                                  =models.ForeignKey(
        userInformation, 
        on_delete=models.CASCADE,
        default=None
     )
    
    insertion_time                  =models.DateTimeField(auto_now=True, auto_now_add=False)
    last_updated                    =models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.product_Name
    
    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        elif not self.last_updated is not None:
            self.last_updated = None
        super(commodities_production, self).save(*args, **kwargs)



#Import product table
class commodities_import(models.Model):

    product_Name                       =models.CharField(max_length=80,choices=Product_Choices)
    import_quantity                    =models.DecimalField(max_digits=9, decimal_places=2)
    import_cost                        =models.DecimalField(max_digits=9, decimal_places=2)
    import_place                       =models.CharField(max_length=150)
    import_date                        =models.CharField(max_length=30)
    importer_name                      =models.CharField(max_length=30)
    importer_mobile_number             =models.CharField(max_length=30)
    email                              =models.ForeignKey(
        userInformation, 
        on_delete=models.CASCADE,
        default=None,
       
     )
    
    insertion_time                  =models.DateTimeField(auto_now=True, auto_now_add=False)
    last_updated                    =models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.product_Name
    
    def save(self, *args, **kwargs):
        if self.last_updated is None:
            self.last_updated = timezone.now()
        elif not self.last_updated is not None:
            self.last_updated = None
        super(commodities_import, self).save(*args, **kwargs)