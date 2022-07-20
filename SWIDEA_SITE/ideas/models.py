from django.conf import settings
from django.db import models
from django.utils import timezone

class Tool(models.Model):
    #이름, 종류, 설명
    name = models.CharField(max_length=50, verbose_name="이름")
    type = models.CharField(max_length=50, verbose_name="종류")
    description = models.TextField(verbose_name="설명")

tool = Tool.objects.all()
TOOL_CHOICES = [(None,'------')]
for t in tool:
    temp = []
    temp.append(t.name)
    temp.append(t.name)
    temp = tuple(temp)
    TOOL_CHOICES.append(temp)
TOOL_CHOICES=tuple(TOOL_CHOICES)

class Idea(models.Model):
    #아이디어명, 이미지, 아이디어 설명, 아이디어 관심도, 예상 개발툴
    name = models.CharField(max_length=50, verbose_name="이름")
    image = models.ImageField(blank=True, upload_to='ideas/%y%m%d', verbose_name="이미지")
    description = models.TextField(verbose_name="설명")
    interest = models.IntegerField(verbose_name="관심도")
    tool = models.CharField(max_length=50, choices=TOOL_CHOICES, verbose_name="개발툴", null=True)
    