from django.db import models

class DateAbstractModel(models.Model):
    create_Date=models.DateTimeField(auto_now_add=True)
    edit_Date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True