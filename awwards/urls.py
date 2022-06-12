from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login/',views.loginuser,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutuser,name='logout'),

    path('profile/<id>/',views.profile,name='user_profile'),

    path('<id>/',views.project_details,name='project-details'),
    path('create_project/new/',views.create_project,name='create_project'),
    path('like_image/<user_id>/<project_id>',views.like_project, name='like_project'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
]