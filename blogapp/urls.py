
from django.urls import path,include
from .views import CategoryListCV,CategoryDetailCV,PostMVS
from rest_framework import routers


router=routers.DefaultRouter()
router.register("post",PostMVS)

urlpatterns = [
    
	path('category/',CategoryListCV.as_view()),
	path('category/<int:pk>',CategoryDetailCV.as_view()),
	# path('cat/<int:pk>',CategoryCV.as_view())
	#!mvs için böyle yazdık
	# path('',include(router.urls))

]

urlpatterns += router.urls