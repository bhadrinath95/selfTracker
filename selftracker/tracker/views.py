from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import CycleTracker, ActionPlanner, Reminder, Preparation, Interview
from .forms import GenerateCycleForm, ActionPlannerForm, ReminderForm, PreparationForm, InterviewForm
from django.http import HttpResponse
from io import BytesIO
import xlwt
from django.core.mail import EmailMessage

# Create your views here.
class export_cycle_xls(View):
    def get(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="cycle.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Cycle')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Start_time', 'Time_taken', 'Distance', 'Max_speed', 'Average_speed', 'Calories' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = CycleTracker.objects.filter(user=request.user).values_list('user', 'date', 'start_time', 'time_taken', 'distance', 'max_speed', 'average_speed', 'calories')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                elif col_num == 2 or col_num == 3:
                    date_time = row[col_num].strftime('%H:%M:%S')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Cycle Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('cycle.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
    def post(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="cycle.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Cycle')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Start_time', 'Time_taken', 'Distance', 'Max_speed', 'Average_speed', 'Calories' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = CycleTracker.objects.filter(user=request.user).values_list('user', 'date', 'start_time', 'time_taken', 'distance', 'max_speed', 'average_speed', 'calories')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                elif col_num == 2 or col_num == 3:
                    date_time = row[col_num].strftime('%H:%M:%S')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Cycle Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        print(request.user.email)
        email.attach('cycle.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
class export_action_xls(View):
    def get(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="action.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Action')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = ActionPlanner.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Action Planner Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('action.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
    def post(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="action.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Action')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = ActionPlanner.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Action Planner Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('action.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response

class export_prepare_xls(View):
    def get(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="prepare.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Prepare')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Preparation.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Preparation Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('prepare.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
    def post(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="prepare.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Prepare')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Preparation.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Preparation Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('prepare.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
class export_todo_xls(View):
    def get(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="todo.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('ToDo')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description', 'Status' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Reminder.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Reminder Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('todo.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
    def post(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="todo.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('ToDo')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Title', 'Description', 'Status' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Reminder.objects.filter(user=request.user).values_list('user', 'date', 'title', 'description', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Reminder Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('todo.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
class export_interview_xls(View):
    def get(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="interview.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Interview')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Company', 'Role', 'Round', 'Description', 'Status' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Interview.objects.filter(user=request.user).values_list('user', 'date', 'company', 'role', 'round', 'description', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Interview Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('interview.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
    
    def post(self, request):
        emailfile = BytesIO()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="interview.xls"'
    
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Interview')
    
        # Sheet header, first row
        row_num = 0
    
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
    
        columns = ['User', 'Date', 'Company', 'Role', 'Round', 'Description', 'Status' ]
    
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
    
        rows = Interview.objects.filter(user=request.user).values_list('user', 'date', 'company', 'role', 'round', 'description', 'status')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 1:
                    date_time = row[col_num].strftime('%Y-%m-%d')
                    ws.write(row_num, col_num, date_time, font_style)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style)
    
        wb.save(response)
        wb.save(emailfile)
        
        email = EmailMessage()
        email.subject = 'Interview Backup'
        email.body = 'Please find the attached xls file'
        email.to = [request.user.email] 
        email.attach('interview.xls', emailfile.getvalue(), 'application/ms-excel')
        email.send(fail_silently=True)
        
        return response
        
class Register(View):
    def get(self,request):
        form=UserCreationForm
        return render(request,'registration/register.html',{'form':form})
    
    def post(self,request):
        saveForm=UserCreationForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'User is created successfully')
        else:
            messages.error(request,'User creation is failed')
        return redirect('/accounts/register')
    
class Home(View):
    template_name='home.html'
    def get(self,request):
        return render(request,self.template_name,{})
    
class Cycle(View):
    template_name='cycle.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = GenerateCycleForm(None)
        cycle_obj = CycleTracker.objects.filter(user=request.user)
        return render(request,self.template_name,{"cycles": cycle_obj,"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = GenerateCycleForm(request.POST)
            if saveForm.is_valid():
                saveForm.save()
                messages.success(request,'Record is created successfully')
            else:
                messages.error(request,'Record creation is failed')
            form = GenerateCycleForm(None)
            cycle_obj = CycleTracker.objects.filter(user=request.user).order_by("date")
            return render(request,self.template_name,{"cycles": cycle_obj,"form": form})
        
class Prepare(View):
    template_name='prepare.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = PreparationForm(None)
        prepare_obj = Preparation.objects.filter(user=request.user)
        return render(request,self.template_name,{"prepares": prepare_obj,"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = PreparationForm(request.POST)
            if saveForm.is_valid():
                saveForm.save()
                messages.success(request,'Record is created successfully')
            else:
                messages.error(request,'Record creation is failed')
            form = PreparationForm(None)
            prepare_obj = Preparation.objects.filter(user=request.user).order_by("date")
            return render(request,self.template_name,{"prepares": prepare_obj,"form": form})
        
class InterviewView(View):
    template_name='interview.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = InterviewForm(None)
        interview_obj = Interview.objects.filter(user=request.user)
        return render(request,self.template_name,{"interviews": interview_obj,"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = InterviewForm(request.POST)
            if request.POST.get("NewItem"):
                saveForm = InterviewForm(request.POST)
                if saveForm.is_valid():
                    saveForm.save()
                    messages.success(request,'Record is created successfully')
                else:
                    messages.error(request,'Record creation is failed')
                form = InterviewForm(None)
                interview_obj = Interview.objects.filter(user=request.user).order_by("date")
                return render(request,self.template_name,{"interviews": interview_obj,"form": form})
            elif request.POST.get("EditItem"):
                edititem = Interview.objects.get(id= request.POST.get("EditItem", ""))
                Interview.objects.get(id= request.POST.get("EditItem", "")).delete()
                form = InterviewForm(instance = edititem)
                interview_obj = Interview.objects.filter(user=request.user).order_by("date")
                return render(request,self.template_name,{"interviews": interview_obj,"form": form})

class Action(View):
    template_name='actionplanner.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = ActionPlannerForm(None)
        action_obj = ActionPlanner.objects.filter(user=request.user)
        return render(request,self.template_name,{"actions": action_obj,"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = ActionPlannerForm(request.POST)
            if saveForm.is_valid():
                saveForm.save()
                messages.success(request,'Record is created successfully')
            else:
                messages.error(request,'Record creation is failed')
            form = ActionPlannerForm(None)
            action_obj = ActionPlanner.objects.filter(user=request.user).order_by("date")
            return render(request,self.template_name,{"actions": action_obj,"form": form})
        
class ToDo(View):
    template_name='reminder.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = ReminderForm(None)
        reminder_obj = Reminder.objects.filter(user=request.user).filter(status=False).order_by("date")
        return render(request,self.template_name,{"reminders": reminder_obj,"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            saveForm = ReminderForm(request.POST)
            if request.POST.get("NewItem"):
                if saveForm.is_valid():
                    saveForm.save()
                    messages.success(request,'Record is created successfully')
                else:
                    messages.error(request,'Record creation is failed')
                form = ReminderForm(None)
                reminder_obj = Reminder.objects.filter(user=request.user).filter(status=False).order_by("date")
                return render(request,self.template_name,{"reminders": reminder_obj,"form": form})
            elif request.POST.get("EditItem"):
                edititem = Reminder.objects.get(id= request.POST.get("EditItem", ""))
                Reminder.objects.get(id= request.POST.get("EditItem", "")).delete()
                form = ReminderForm(instance = edititem)
                reminder_obj = Reminder.objects.filter(user=request.user).filter(status=False).order_by("date")
                return render(request,self.template_name,{"reminders": reminder_obj,"form": form})