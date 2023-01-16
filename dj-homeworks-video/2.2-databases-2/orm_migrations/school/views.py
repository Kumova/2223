from django.views.generic import ListView
from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    context_object_name = 'students_list'
    queryset = Student.objects.filter(student__group='group')
    return render(request, template, context)


 #   def students_list(request):
 #        template = 'school/students_list.html'
 #        context = {}
 #        context_object_name = 'students_list'
 #        ordering=Student.objects.order_by('group')
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
   #      ordering = 'group'

   #      return render(request, template, context)

