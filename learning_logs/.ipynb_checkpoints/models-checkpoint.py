from django.db import models
#关联用户
from django.contrib.auth.models import User

class Topic(models.Model):
    """用户学习的主题"""
    #设置200字符
    text = models.CharField(max_length = 200)
    #记录日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    #关联用户
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        """返回模型的字符串表示"""
        #添加主题与所有者的名字
        return f"{self.text} by {self.owner.username}"

class Entry(models.Model):
    """学到的有关莫个主题的具体知识"""
    #外键引用数据库中的林外一个记录，将两者关联
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)  # 添加 on_delete 参数是Django 2.0+ 的推荐做法 
    text = models.TextField()
    #按照创建顺序显示条目，并将每个条目旁加入时间辍
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #用Entries表示多个条目，而不是Entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        #18-2如果长度少于50,没有省略号
        if len(self.text) <= 50:
            return self.text
        else:#显示前50字符，并添加省略号
            return self.text[:50] + "..."