from django.db import models

# Create your models here.
class MenuInMenu(models.Model):
    name = models.CharField(max_length=255, null=False, db_index=True)
    previous = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
