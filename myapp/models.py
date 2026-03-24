from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)         # Primary key field
    name = models.CharField(max_length=100)                  # Patient Name (as used in template & views)
    age = models.IntegerField()                              # Age (instead of 'agc' - template has 'Age')
    gender = models.CharField(max_length=10)                 # Gender
    height = models.FloatField()                              # Height in ft
    weight = models.FloatField()                              # Weight in kg
    address = models.TextField()                              # Address
    phone = models.CharField(max_length=15)                  # Phone Number
    email = models.EmailField()                               # Email Id
    date = models.DateField()                                 # Date
    disease = models.CharField(max_length=100, blank=True)   # Disease (optional)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Treatment cost (optional)

    def __str__(self):
        return self.name