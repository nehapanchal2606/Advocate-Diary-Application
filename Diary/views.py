from csv import Dialect
from fnmatch import fnmatch
from gettext import lngettext
from urllib import request
from django.shortcuts import render, redirect
from .models import Diary
from datetime import datetime
# Create your views here.
from django.db.models import Q

# def add_diary(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('First_name')
#         lastname = request.POST.get('Last_name')
#         c_number = request.POST.get('case_number')
#         date = request.POST.get('case_Date')
#         des = request.POST.get('case_des')

#         case = Diary(First_name = firstname, Last_name=lastname, case_number=c_number, case_Date = date, case_des=des)
#         case.save()
#         return redirect('/List_case/')

#     else:
#         pass

#     return render(request, 'add_diary.html')


def search_case(request):
    query = request.POST.get('date')
    data = Diary.objects.filter(Q(case_Date=query))
    print('mydata',data)
    for val in data:
        print(val.id)
    return render(request, 'search_case.html', {'data':data})
        
def List_case(request):
    all_case = Diary.objects.all()
    return render(request,'admin_inbox.html', {'all_case':all_case})

def edit_case(request, id):
    ed = Diary.objects.get(id=id)
    fn = request.POST.get('First_name')
    ln = request.POST.get('Last_name')
    cn = request.POST.get('case_number')
    cdate = request.POST.get('case_Date')
    cd = request.POST.get('case_des')
    da=ed.case_Date
    if request.method == 'POST':
        ed.First_name = fn
        ed.Last_name = ln
        ed.case_number = cn
        ed.case_Date = cdate
        ed.case_des = cd
        ed.save()
        return redirect('/')
    return render(request,'edit_case.html', {'edit':ed, 'da':da})

def delete_case(request,id):
    dele = Diary.objects.get(id=id)
    dele.delete()
    return redirect('/')

def post(request):
    if request.method == 'POST':
        firstname = request.POST.get('First_name')
        lastname = request.POST.get('Last_name')
        c_number = request.POST.get('case_number')
        date = request.POST.get('case_Date')
        des = request.POST.get('case_des')

        case = Diary(First_name = firstname, Last_name=lastname, case_number=c_number, case_Date = date, case_des=des)
        case.save()
        return redirect('/')

    else:
        pass
    return render(request, 'admin_post.html')