from django.urls import path

from . import views
app_name = 'events'


urlpatterns = [
    path('', views.index, name='index'),
    #events/eventid/
    path('<int:pk>/', views.DetailView.as_view(),name='detail'),
   
    #events/event/add
    path('event/add',views.EventCreate.as_view(),name='event-add'),

    #events/event/2
    path('event/<int:pk>',views.EventUpdate.as_view(),name='event-update'),

    #events/event/val/delete/
    path('event/<int:pk>/delete',views.EventDelete.as_view(),name='event-delete'),

    #events/tasks
    path('tasks',views.TasksView, name='tasks'),

    #events/task/add
    path('task/add',views.TaskCreate.as_view(),name='task-add'),

    #events/task/edit
    path('task/<int:pk>',views.TaskUpdate.as_view(),name='task-update'),

    #events/task/val/delete/
    path('task/<int:pk>/delete',views.TaskDelete.as_view(),name='task-delete'),
    
    #events/notes
    path('notes',views.NotesView,name='notes'),
    
    #events/note/add
    path('note/add',views.NoteCreate.as_view(),name='note-add'),

    #events/note/edit
    path('note/<int:pk>',views.NoteUpdate.as_view(),name='note-update'),

    #events/note/val/delete/
    path('note/<int:pk>/delete',views.NoteDelete.as_view(),name='note-delete'),

    #register
    path('register', views.UserFormView.as_view(), name='register'),

    #login
    path('login', views.LoginView.as_view(), name='login_request'),

    #logout
    path('logout/', views.LogOutView.as_view(), name='logout'),

    #search
    path('search', views.search, name='search'),
]