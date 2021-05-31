from django.db import models
from django.contrib.auth.models import User
from deneme.models import articlesModel
from deneme.abstract_models import DateAbstractModel

class commentModel(DateAbstractModel):
    
    writer=models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    article= models.ForeignKey(articlesModel, on_delete=models.CASCADE, related_name='comments')
    comment= models.TextField()

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural= 'Comments'
    def __str__(self):
        return self.writer.username

