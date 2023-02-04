from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse
from . import fields

class ElecUnits(models.Model):
    YN=[
        (1, 'Yes'),
        (0, 'No')
    ]
    no = models.AutoField(db_column='No', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(default=timezone.now)  # This field type is a guess.
    prevdateinmillisec = fields.myTimestampField( db_column='prevDateInMilliSec', blank=True, null=True)  # Field name made lowercase.
    nextdateinmillisec = fields.myTimestampField( db_column='nextDateInMilliSec', blank=True, null=True)  # Field name made lowercase.
    # nextdateinmillisec = models.BigIntegerField( db_column='nextDateInMilliSec', blank=True, null=True)  # Field name made lowercase.
    prevreading = models.IntegerField(db_column='prevReading', blank=True, null=True)  # Field name made lowercase.
    nextreading = models.IntegerField(db_column='nextReading', blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(max_length=15, blank=True, null=True)
    calcstr = models.CharField(db_column='calcStr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isitbill = models.IntegerField(default=0, choices=YN, db_column='isItBill', blank=False, null=False)  # Field name made lowercase.
   
    def __str__(self):
        return self.calcstr
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        db_table = "elecUnits"