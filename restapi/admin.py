from django.contrib import admin
from .models import Teacher, Subject, Question, Student, Comment, Answer

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Comment)
admin.site.register(Answer)