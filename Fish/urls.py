from django.urls import path
from rest_framework import routers
from .views import Image_view, waterBodies_View,Species_View,Nearest,GCD_View

router = routers.SimpleRouter()
router.register(r'species',Species_View,basename="species")
router.register(r'waterbodies',waterBodies_View,basename="waterbodies"), 

urlpatterns =[
    path(r"get_images/<str:name>",Image_view,name="get_images"),  
    path(r"find_nearest/<int:pk>",Nearest,name="find_nearest"),
    path(r"GCD",GCD_View,name="GCD"),
]
urlpatterns+=router.urls