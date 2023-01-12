from django.db import models

# Create your models here.
class Tickit(models.Model):
    btitle=models.CharField(max_length=50)
    cat=models.IntegerField()
    # isbn=models.IntegerField()
    Aname=models.IntegerField()
    # active=models.IntegerField()
    is_deleted=models.CharField(max_length=5)
    uid=models.IntegerField()

    def __str__(self):

        return self.btitle
    