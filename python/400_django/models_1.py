from django.db import models


class Animal(models.Model):
    updated_at = models.CharField(
        auto_now=True,
        help_text='更新时间',
        null=True,
        choices=((0, "已删除"), (1, "正常")),
        max_length=128,
        default=0
    )
