from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("Avinash",views.avinash,name="Avinash"),
    path("Akash",views.akash,name="Akash")
]