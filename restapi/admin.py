from django.contrib import admin
from .models import Teacher, Subject, Question, Student, Answer, StudentTokenModel

admin.site.site_header = 'Админ панель'

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'subject', 'teacher', 'create_date')

class TokensAdmin(admin.ModelAdmin):
    list_display = ('key', 'student', 'created')

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Answer, AnswersAdmin)
admin.site.register(StudentTokenModel, TokensAdmin)