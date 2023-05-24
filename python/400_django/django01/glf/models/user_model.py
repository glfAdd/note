from django.db import models


class UserModels(models.Model):
    user_name: str = models.CharField(max_length=100)
    age: int = models.IntegerField()
    sex_choice = (
        (0, '女'),
        (1, '男'),
    )
    # ????? django 会自动生成 get_sex_display() 函数
    sex = models.IntegerField(choices=sex_choice, default=1)

    # serializer 的 source 可以调用这个函数
    def get_user_name(self):
        return self.user_name + 'XiaoMing'

    class Meta:
        # 设置表名
        db_table = 'user'
