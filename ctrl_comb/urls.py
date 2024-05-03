from django.urls import path
from .views import * 

urlpatterns = [
    path('mark/',MarkList.as_view(),name="mark_list"),
    path('mark/save',mark_save,name="mark_save"),
    path('mark/delete/<int:pk>',mark_delete,name="mark_delete"),
    path('mark/edit/<int:pk>',mark_edit,name="mark_edit"),
    
    path('models/',ModeloList.as_view(),name="modelo_list"),
    path('models/new',ModeloNew.as_view(),name="modelo_new"),
    path('models/<int:pk>',ModeloEdit.as_view(),name="modelo_edit"),
    path('models/delete/<int:pk>',ModeloDelete.as_view(),name="modelo_delete"),
    path('models/modal/<int:pk>',ModeloEditModal.as_view(),name="modelo_edit_modal"),
    path('models/modal/new',ModeloNewModal.as_view(),name="modelo_new_modal"),

    path('models/dt',modelo_dt,name="modelo_dt"),
]