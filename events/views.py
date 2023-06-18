from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import HttpResponse

from django.template import loader

from django.views.generic import View

from .forms import UserForm, LoginForm
from .models import Event, Task, Note

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q

def index(request):
    event_list = Event.objects.order_by('start')
    context ={
        'event_list': event_list
    }
    return render(request,'events/index.html',context)
    
class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'description', 'type', 'start', 'location', 'duration' ]

class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'description', 'type', 'start', 'location', 'duration' ]

class EventDelete(DeleteView):
    model = Event
    success_url= reverse_lazy('events:index')

def TasksView(request):
    task_list = Task.objects.order_by('name')
    context ={
        'task_list': task_list
    }
    return render(request,'events/tasks.html',context)

class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'event']

class TaskUpdate(UpdateView):
    model = Task
    fields = ['name', 'event']

class TaskDelete(DeleteView):
    model = Task
    success_url= reverse_lazy('events:index')

def NotesView(request):
    notes_list = Note.objects.order_by('details')[:5]# TODO: Why five though
    context ={
        'notes_list': notes_list
    }
    return render(request,'events/notes.html',context)

class NoteCreate(CreateView):
    model = Note
    fields = ['details']

class NoteUpdate(UpdateView):
    model = Note
    fields = ['name', 'description']

class NoteDelete(DeleteView):
    model = Note
    success_url= reverse_lazy('events:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'events/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # add user to the database to create new user
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #change password
            # user.set_password("new_P4ssword")
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)#logged in user
                    #request.user.username => to get the logged in user's information
                    return redirect('events:index')
        return render(request, self.template_name, {'form':form})
class LoginView(View):
    #display blank form
    form_class = LoginForm
    template_name = 'events/login_form.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        #if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)    
        # print(user)
        if user is not None:
            login(request,user)
            #if user.is_active:
            login(request,user)#logged in user
            # m = .objects.get(username=request.POST['username'])
            if user.check_password(request.POST['username']):
                request.session['user_id'] = user.get_username()
                # return HttpResponse('You\'re logged in.')
                #request.user.username => to get the logged in user's information
                messages.info(request, "You have been successfully logged in")
                print("Logged in?", request.session['user_id'])
                return redirect('events:index')
            else:
                messages.info(request, "Incorrect credentials")#TODO: Messages as toast or clearer
        return redirect('events:index')
class LogOutView(View):
    def get(self,request):
        try:
            # print("Sessions", request.session['user_id'])
            del request.session['user_id']
            # del request.session['member_id']
            logout(request)
            messages.info(request, "You have been successfully logged out")
        except KeyError:
            print("Error logging out")
        return redirect('events:index')
# TODO: Class versus function
class search(View):
    #TODO: Search whole site
    search_term = request.GET["query"]
    print(search_term)
    event_list = Event.objects.filter(name__icontains=search_term)
    event_list = Event.objects.order_by('description')
    context ={
        'event_list': event_list
    }
    print("Event List: ", event_list)
    redirect(request,'events/index.html',context)