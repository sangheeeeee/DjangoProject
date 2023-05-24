# 테이블 생성하는 곳 > model.py에서 함
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  #__str__메소드는 객체의 정보를? 문자를? 보여주는 메소드이다
        return self.question_text  #models를 수정하면 makemigrations > migrate를 해야하지만, 관리자 화면에서 데이터베이스 모델 건드리지 않고 pub_date를 추가로 보여지게 하고자 한다.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #on_delete: 해당 데이터가 삭제됐을때 나머지 데이터도 다 삭제되는 코드
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

