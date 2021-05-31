from django.db import models

class contactModel(models.Model):
    email= models.EmailField(max_length=250, blank=False, )
    name_lastname = models.CharField(max_length=150)
    message = models.TextField()
    create_Date=models.DateTimeField(auto_now_add=True)
    edit_Date=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact'
        verbose_name= 'Contact'
        verbose_name_plural= 'Contacts     '
    def __str__(self):
        return self.email