from django.contrib import admin
from .models import Teacher, Subject, Question, Answer, Student

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)