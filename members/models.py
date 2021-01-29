# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Members(models.Model):
    userid = models.CharField(max_length=64, verbose_name="아이디")
    userpassword = models.CharField(max_length=64, verbose_name="비밀번호")
    useremail = models.EmailField(max_length=128, verbose_name="이메일")
    created = models.DateTimeField(auto_now_add=True, verbose_name="가입일시")
    update = models.DateTimeField(auto_now_add=True, verbose_name="수정일시")
    
    class Meta:
        db_table = "store user"
        verbose_name="이용고객"
    
class product(models.Model):
    food=models.CharField(max_length=128, verbose_name="상품이름")
    price=models.CharField(max_length=64, verbose_name="가격")
    images=models.CharField(max_length=64, verbose_name="이미지파일")
    type=models.CharField(max_length=64, verbose_name="종류")
