from django.contrib import admin
from .models import Teacher, Subject, Question, Student, Answer

admin.site.site_header = 'Админ панель'

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Answer)