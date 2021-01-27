from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import CycleTracker, ActionPlanner, Reminder
from .forms import GenerateCycleForm, ActionPlannerForm, ReminderForm

# Create your views here.
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