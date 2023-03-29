
from django.urls import path
from .views import GetAllProjectsView, UpdateProjectView

urlpatterns = [
    
    path('projects', GetAllProjectsView.as_view(), name='projects'),
     path('edit-project/<int:pk>', UpdateProjectView.as_view(), name='edit_project'),
    
]