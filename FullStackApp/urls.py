

from django.contrib import admin
from django.urls import path,include
from djangoapi import views
#from myapp.views import Articless
from djangoapi.views import departmentApi
from rest_framework.routers import DefaultRouter
#Article_detail
router=DefaultRouter()
router.register('department',departmentApi,basename='department')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('article/',views.Articless),
    #path ('article/<int:pk>',views.article_detail),
    #path('article/',Articless.as_view()),
    #path('article/<int:id>',Article_detail.as_view())
    path('',include(router.urls)),

]