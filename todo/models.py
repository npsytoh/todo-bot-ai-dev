import enum
from django.db import models


class Priorities(enum.IntEnum):
    Nothing = 0
    Low = 1
    Middle = 2
    High = 3

    @classmethod
    def get_priorities(cls):
        return tuple((x.value, x.name) for x in cls)

class TodoItems(models.Model):
    task_id = models.SlugField(max_length=10)
    task_title = models.CharField(verbose_name='タイトル', max_length=255)
    task_description = models.TextField(verbose_name='詳細', default='', null=True, blank=True)
    status = models.BooleanField(verbose_name='ステータス', default=False)
    is_important = models.BooleanField(verbose_name='重要度', default=False)
    priority = models.SmallIntegerField(verbose_name='優先度', default=0, choices=Priorities.get_priorities())
    due_date = models.DateField(verbose_name='期限日', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    completed_at = models.DateTimeField(verbose_name='完了日', null=True, blank=True)

    class Meta:
        verbose_name = 'ToDo Item'
        verbose_name_plural = 'ToDo Items'

    def __str__(self):
        return self.task_title
