from django.contrib import admin
from django.urls import path
from To_Do_List import views

urlpatterns = [
    # Home page
    path('', views.index, name="todo"),
    
    # Path to delete a to-do item using its primary key (item_id)
    path('del/<str:item_id>/', views.remove, name="del"),
    
    # Path to update a to-do item using its primary key (item_id)
    path('update/<str:item_id>/', views.update, name="update"),
    
    # Admin site
    path('admin/', admin.site.urls),
]
