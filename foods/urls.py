from . import views
from django.urls import path

app_name = 'foods'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),

    path('add',views.create_item,name='create_item'),
path('delete/<int:id>/',views.delete_item,name='delete_item'),

    path('update/<int:id>/', views.update_item, name='update_item'),
    path('aboutus/',views.aboutus,name='aboutus'),
]
