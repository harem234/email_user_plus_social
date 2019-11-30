from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # caller (calls google api) and assign the redirect from the google by the next_call argument
    path('google/api_caller/<str:next_call>/', views.google_call, name='google_call'),
    # call backs from google api (use these url names in <str:next_call> in the upper)
    path('google/callback/signup/', views.google_callback_signup, name='google_callback_signup'),
    path('google/callback/login/', views.google_callback_login, name='google_callback_login'),
    path('google/callback/add_social/', views.google_callback_add_social, name='google_callback_add_social'),
    path('google/callback/revoke/', views.google_callback_revoke, name='google_callback_revoke'),
    # end of call backs
    # google_ajax_url_name: is the name of url witch be called by ajax json post request
    path('google/ajax_to_post/<str:google_ajax_url_name>/', views.TemplateCSRFView.as_view(), name='google_ajax'),
    # call from js api through ajax POST json
    path('google/ajax_post/signup/', views.GoogleAjaxSignupView.as_view(), name='google_ajax_signup'),
    path('google/ajax_post/login/', views.GoogleAjaxLoginView.as_view(), name='google_ajax_login'),
    path('google/ajax_post/add_social/', views.GoogleAjaxAddSocialView.as_view(), name='google_ajax_add_social'),
    # end of ajax POST JSON

    path('google/', TemplateView.as_view(template_name='oauth2_google/google_ajax.html'), name='google'),

    path('google/error/', TemplateView.as_view(template_name='oauth2_google/google_ajax.html', ), name='google_error'),
]
