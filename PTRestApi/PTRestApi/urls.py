from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.TodoList.as_view()),
    path('api/<str:nombre>/',views.TodoList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
