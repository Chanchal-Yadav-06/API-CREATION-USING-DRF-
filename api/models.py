from django.db import models

# Create your models here.

class companies(models.Model):
    company_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Location=models.CharField(max_length=50)
    About=models.TextField()
    Type=models.CharField(max_length=20,choices=[('IT','IT'),
                                                 ('NON TECH','NON TECH'),
                                                 ('MOBILE APP','MOBILE APP'),
                                                 ('AUTOMATION','AUTOMATION')])
    Active=models.BooleanField(default=True)


    def __str__(self):
        return self.Name