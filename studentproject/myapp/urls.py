from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Add_student/', views.add_student, name='add_student'),
    path('student_class/', views.student_class, name='student_class'),
    path('student_view/<slug:slug>/', views.student_view, name='student_view'),
    path('student_update/<slug:slug>', views.update_view, name="student_update"),
    path('delete_student/<slug:slug>', views.delete_student, name="delete_student"),
    path('student_profile/<slug:slug>',views.student_profile, name="student_profile"),
    path('section_add/',views.section_add, name="section_add"),
    path('class_add/',views.class_add, name="class_add")
    # path('load/', views.load_students, name='student_class'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)