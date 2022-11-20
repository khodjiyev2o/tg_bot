from django.db import models

# Create your models here.




class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    

    def __str__(self):
        if self.username:
            return f"{self.id} - @{self.username}"
        else:
            return f"{self.id} - {self.full_name}"
class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"№{self.id} - {self.user_id}"

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    companyname = models.CharField(verbose_name="Kompaniya nomi", max_length=50)
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Kompaniya haqida", max_length=3000,blank=True,default="None")
    employer_name = models.ForeignKey(Employer,on_delete=models.CASCADE,verbose_name="Ish beruvchi",max_length=20)    

    def __str__(self):
        return f"№{self.id} - {self.companyname}"



class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Ism", max_length=100)
    phone_number = models.IntegerField(verbose_name="Telefon raqam")
    card_number = models.IntegerField(verbose_name="Karta Raqami")
    bank_name = models.CharField(verbose_name="Bank Nomi", max_length=100)

    def __str__(self):
        return str(self.name)




class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
    employer = models.ForeignKey(Employer,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"№{self.id} - {self.user_id}"
    
    