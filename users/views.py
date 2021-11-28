from django.shortcuts import render
from django.http import HttpResponse ,Http404
from users.models import Manager,Teacher,Student
# Create your views here.

def get_index(request):
    return HttpResponse('users index')
    #return render(request,'hello.html')


def signup_manager(request):
    user_id = request.Post['user_id']
    try :
        manager = Manager.objects.get(user_id = user_id) 
    except Manager.DoesNotExist:
        raise Http404('מנהל לא קיים במערכת. אנא פנה למנהל המערכת')
    name = request.Post['name']
    phone_number = request.Post['phone_number']
    school = request.Post['school']
    password = request.Post['psw']
    
    Manager.objects.get(user_id = user_id).delete() #delete the object that we created earlier
    manager = Manager(name = name,password = password,user_id = ID, phone_number = phone_num,school=school)
    manager.save()
    return render(request,'homepage/index.html')



def get_chooseprofile(request):
    return render(request,'chooseprofile.html')