from django.urls import path
from . import views
urlpatterns = [
    # path("index",views.index, name="index")
     path("",views.ListProductAPIView.as_view(),name="Product_list"),
     path("create/", views.CreateProductAPIView.as_view(),name="Product_create"),
     path("delete/<int:pk>", views.DestroyProductAPIView.as_view(),name="Product_Delete"),
     path("upgrade/<int:pk>", views.UpgradeProductAPIView.as_view(),name="Product_upgrade"),


]
