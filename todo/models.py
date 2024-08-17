from django.db import models


class TodoItems(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=255)
    description = models.TextField(verbose_name='内容', default='', null=True, blank=True)
    is_completed = models.BooleanField(verbose_name='完了', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ToDo Item'
        verbose_name_plural = 'ToDo Items'

    def __str__(self):
	    return self.title
