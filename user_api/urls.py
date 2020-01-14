from unicodedata import name

from django.urls import path, reverse_lazy
from user_api import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('update/', views.UpdateUserView.as_view(), name='update'),
    path('deactivate/', views.DeactivateUserView.as_view(), name='Deactivate'),

    path('token/', views.CreateTokenView.as_view(), name='token'),
]
