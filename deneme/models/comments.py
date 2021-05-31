from django.db import models
from django.contrib.auth.models import User
from deneme.models import articlesModel

class commentModel(models.Model):
    
    writer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    article= models.ForeignKey(articlesModel, on_delete=models.CASCADE, related_name='comments')
    comment= models.TextField()
    create_Date=models.DateTimeField(auto_now_add=True)
    edit_Date=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural= 'Comments'
    def __str__(self):
        return self.writer.username

