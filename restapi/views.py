from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Answer, Subject, Teacher
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

# Answers 
def result(request):
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

  # while n < len(rates):
    # content.append(rates[n]) 

  results_doc.build(content)
  print(answers)
  pdf_buffer.seek(0)
  if request.user.is_authenticated:
    return FileResponse(pdf_buffer, as_attachment=False, filename='results.pdf')
  else:
    return HttpResponseRedirect('login')

def subjects(request):
  subjects = Subject.objects.all()
  teachers = Teacher.objects.all()

  context = {
    'subjects': subjects,
    'teachers': teachers
  }

  return render(request, 'restapi/subjects.html', context)

def teachers(request, id):
  subjects = Subject.objects.all()
  teachers = Teacher.objects.all()
  teachersSorted = []
  teacherSubs = []

  context = {
    'subjects': subjects,
    'teachers': teachersSorted
  }
  
  i = 0

  for teacher in teachers:
      while i < len(teacher.subject.values()):
          teacherSubs.append(teacher.subject.values()[i]['subject_id'])

  print('TeacherSubs:', teacherSubs)
  print('Teachers Sorted: ', teachersSorted)

  return render(request, 'restapi/teachers.html', context)