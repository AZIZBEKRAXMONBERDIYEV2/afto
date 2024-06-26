from django.db import models

class Aftosalon(models.Model):
 
    brent=models.CharField(max_length=15)
    model=models.CharField(max_length=10)
    rang =models.CharField(max_length=10)
    yil  = models.IntegerField()
    narx =models.FloatField()
    rasmi=models.CharField(max_length=255)
    quvati=models.IntegerField()



    def __str__(self):
        return f"{self.brent} {self.model} {self.rang} {self.yil}"
    

    def to_dict(self):
        """
        Convert model to dictionary
        """
        return {
            'id': self.id,
            'brent': self.brent,
            'model': self.model,
            'rang': self.rang,
            'yil': self.yil,
            'narx': self.narx,
            'rasmi': self.rasmi,
            'quvati': self.quvati
        }

