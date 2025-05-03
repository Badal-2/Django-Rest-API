from django.contrib import admin
from django.urls import path,include

from .views import todoview , instaview

from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'todos', todoview)
router.register(r'instas', instaview)



urlpatterns = [
    path('',include(router.urls))
]






