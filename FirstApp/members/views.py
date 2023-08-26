from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers' : members
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  member = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember' : member
  }
  return HttpResponse(template.render(context, request))  

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mymembers
  }
  return HttpResponse(template.render(context, request))