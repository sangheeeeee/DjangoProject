from django.contrib import admin  #venv>lib>site_package>>>>contirb>admin을 import
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

#QuestionAdmin이라는 클래스 하나를 정의하고, fields라는 속성으로 두 개의 테이블의 위치를 임의로 변경하여 지정
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields' : ['question_text']},),
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})]  #question안에있는 model에서 class에 지정된 변수를 넣어줌
    inlines = [ChoiceInline]  #한줄씩 입력받도록 설정, 선택지를 한 화면에 모두 입력할 수 있음/ 저장하면 각각의 데이터베이스(Q,C)에 데이터가 저장된다.
    list_display = ('question_text', 'pub_date') #튜플 형태
    list_filter = ['pub_date'] #리스트 형태, 날짜와 관련된 필터로 자동 생성된다. question_text를 넣으면 생성된 질문과 관련된 필터로 자동 생성된다.
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# 테이블에 내용을 추가할 때 admin에서 한다