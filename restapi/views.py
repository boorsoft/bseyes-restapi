from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Answer, Subject, Teacher
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer
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
    return HttpResponseRedirect('../login')

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
    return HttpResponseRedirect('../../login')  

# Answers 
def result(request, subject_id, teacher_id):
  # fetch data
  answers = Answer.objects.filter(subject=subject_id, teacher=teacher_id)

  pdf_buffer = BytesIO()
  font = "static/fonts/OpenSans-Regular.ttf"
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

  heading_style = style['Heading4']
  heading_style.fontName = 'OpenSansBold'

  page_break = PageBreak()
  space = Spacer(1, 20)

  q_num = 1

  # 1 answer = 1 page
  for answer in answers:
    course = Paragraph('<font name="OpenSansBold">Курс</font> ' + answer.subject.sub_name, body_style)
    teacher = Paragraph('<font name="OpenSansBold">Преподаватель</font> {} {}'.format(answer.teacher.last_name, answer.teacher.first_name), body_style)
    info = Paragraph('1 - Абсолютно не согласен, 5 - Полностью согласен', body_style)
    content.append(course)
    content.append(teacher)
    content.append(space)
    content.append(info)
    content.append(space)

    rates = answer.rate.split(",")

    for question in answer.question.all():
      question = Paragraph(str(q_num) + '. ' + question.question_body, body_style)
      content.append(question)

      for rate in rates:
        rate = Paragraph('<font name="OpenSansBold">Ответ:</font> ' + rate, body_style)
        content.append(rate)
        break

      q_num += 1

    comment_heading = Paragraph('Комментарий: ', heading_style)
    comment = Paragraph(answer.comment, body_style)
    content.append(space)
    content.append(comment_heading)
    content.append(comment)
    q_num = 1
    content.append(page_break)

  results_doc.build(content)
  pdf_buffer.seek(0)
  if request.user.is_authenticated:
    return FileResponse(pdf_buffer, as_attachment=False, filename='results.pdf')
  else:
    return HttpResponseRedirect('../../../../login')