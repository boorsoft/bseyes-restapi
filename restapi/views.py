from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Answer, Subject, Teacher
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

def subjects(request):
  subjects = Subject.objects.all()

  context = {
    'subjects': subjects,
  }

  if request.user.is_authenticated:
    return render(request, 'restapi/subjects.html', context)
  else:
    return HttpResponseRedirect('login')

def teachers(request, id):
  subjects = Subject.objects.all()
  teachers = Teacher.objects.filter(subject = id)

  context = {
    'subjects': subjects,
    'teachers': teachers,
    'subject_id': id
  }

  if request.user.is_authenticated:
    return render(request, 'restapi/teachers.html', context) 
  else:
    return HttpResponseRedirect('login')  

# Answers 
def result(request, subject_id, teacher_id):
  # fetch data
  answers = list(Answer.objects.all())

  pdf_buffer = BytesIO()
  font = "static/fonts/OpenSans-Light.ttf"
  fontBold = "static/fonts/OpenSans-Bold.ttf"
  pdfmetrics.registerFont(TTFont('OpenSans', font))
  pdfmetrics.registerFont(TTFont('OpenSansBold', fontBold))
  
  results_doc = SimpleDocTemplate(pdf_buffer)

  content = []

  style = getSampleStyleSheet()
  # style.list()
  body_style = style['BodyText']
  body_style.fontName = 'OpenSans'
  body_style.fontSize = 10

  title_style = style['Title']
  title_style.fontName = 'OpenSansBold'
  title_style.fontSize = 12

  page_break = PageBreak()
  title = Paragraph("Анкетирование", title_style)
  

  content.append(title)

  i = 1
  n = 0

  for answer in answers:
    question = Paragraph('Вопрос № ' + str(i), body_style)
    rates = answer.rate.split(",")
    print(rates)
    content.append(question)
    i += 1

  results_doc.build(content)
  print(answers)
  pdf_buffer.seek(0)
  if request.user.is_authenticated:
    return FileResponse(pdf_buffer, as_attachment=False, filename='results.pdf')
  else:
    return HttpResponseRedirect('login')