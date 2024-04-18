from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views
from django.conf.urls.static import static
from .views import add_subject, view_subjects, edit_subject, delete_subject
from .views import delete_timetable_entry
from .views import add_class, view_class, myclass_detail
from .views import student_subjects

from .views import view_student_timetable
from .views import get_subjects_for_class





urlpatterns = [
    
    path('',views.home,name='home'),
    
    

    path('student/', views.student_view, name='student'),
    path('permission_denied/', views.permission_denied, name='permission_denied'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('view_subjects/', views.view_subjects, name='view_subjects'),
    
    path('myhome',views.myhome,name='myhome'),
    path('signup',views.signup,name='signup'),
    # path('login',views.user_login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logoutPage'),
    path('StaffReg',views.StaffReg,name='StaffReg'),
    path('StaffpHome',views.StaffpHome,name='StaffpHome'),
    path('about/', views.about,name='about'),
    path('course/', views.course,name='course'),
    path('testimonial/', views.testimonial,name='testimonial'),
     
    path('detail/', views.detail,name='detail'),
     
    path('feature/', views.feature,name='feature'),
     
    path('team/', views.team,name='team'),
    
    path('login/', views.user_login, name='login'),
    
    
    
    path('contact/', views.contact,name='contact'),
    
    
    
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('generate_user/', views.generate_user, name='generate_user'),

    path('slogin/', views.slogin, name='slogin'),
    
    
    path('all_users/', views.all_users, name='all_users'),
    
    
    path('submit_student_details/', views.submit_student_details, name='submit_student_details'),
    
    path('view_student_details/',views. view_student_details, name='view_student_details'),
    
    path('leave_application/',views. leave_application, name='leave_application'),
    
    path('add_student/', views.add_student, name='add_student'),
    
    
    
    path('class_details/<int:class_number>/', views.class_details, name='class_details'),
    
    path('update-students/', views.update_students, name='update_students'),
        
    

    
    path('manage_timetable/', views.manage_timetable, name='manage_timetable'),
    
    path('add_timetable/', views.add_timetable, name='add_timetable'),
    
    path('delete_timetable_entry/<int:timetable_id>/', views.delete_timetable_entry, name='delete_timetable_entry'),
    
    path('register/', views.register_student, name='register_student'),
    
    
    path('create_staff/', views.create_staff, name='create_staff'),
    
    path('staffpage/', views.staff_page, name='staffpage'),
    
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    
    path('add_class/', views.add_class, name='add_class'),
    
    path('view_class/', views.view_class, name='view_class'),
    
    path('class/detail/<int:class_id>/', views.myclass_detail, name='myclass_detail'),  # New URL pattern for MyClass details
    
    path('edit_subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    
    path('student_subjects/', views.student_subjects, name='student_subjects'),
    
   
   
    path('views_student_timetable/', views.view_student_timetable, name='view_student_timetable'),

    path('get-subjects-for-class/<int:class_id>/', get_subjects_for_class, name='get-subjects-for-class'),
    
    path('submit_leave_request/', views.submit_leave_request, name='submit_leave_request'),
    path('view_leave_requests/', views.view_leave_requests, name='view_leave_requests'),
    path('approve_leave_request/<int:leave_id>/', views.approve_leave_request, name='approve_leave_request'),
    path('reject_leave_request/<int:leave_id>/', views.reject_leave_request, name='reject_leave_request'),
    
    path('approve_leave_request/<int:leave_request_id>/', views.approve_leave_request, name='approve_leave_request'),
    path('reject_leave_request/<int:leave_request_id>/', views.reject_leave_request, name='reject_leave_request'),
    
    path('get-subjects-for-day/', views.get_subjects_for_day, name='get_subjects_for_day'),
    
    
    path('staff/', views.staff_view, name='staff_view'),
    
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    
    path('subjects/<int:subject_id>/notes/', views.subject_notes_view, name='subject_notes'),
    
    path('staff-leave-application/', views.staff_leave_application, name='staff_leave_application'),
    path('submit-staff-leave/', views.submit_staff_leave, name='submit_staff_leave'),
    
    path('staff/timetable/', views.view_staff_timetable, name='view_staff_timetable'),
    
    path('staff/view-notes/', views.view_notes, name='view_notes'),
    
    path('staff/edit-note/<int:note_id>/', views.edit_note, name='edit_note'),

    path('manage-staff-leave-requests/', views.manage_staff_leave_requests, name='manage_staff_leave_requests'),
    
    
    path('leave-request/approve/<int:leave_id>/', views.approve_leave_request, name='approve_leave_request'),
    path('leave-request/reject/<int:leave_id>/', views.reject_leave_request, name='reject_leave_request'),
    
    path('attendance/', views.attendance_view, name='attendance_view'),
    
    path('view_attendance/', views.view_attendance, name='view_attendance'),

    path('student/attendance/', views.student_attendance_view, name='student_attendance'),
    
    path('online_class/', views.online_class, name='online_class'),
    
    path('student/online-class/', views.student_online_class, name='student_online_class'),
    
    path('meet-link/<int:subject_id>/', views.view_meet_link, name='meet_link'),
    
    path('subject/<int:subject_id>/meet-link/', views.view_meet_link, name='view_meet_link'),
    
    path('marks/', views.view_marks, name='view_marks'),
    
    path('submit_marks/', views.submit_marks, name='submit_marks'),
    
    path('submit_marks/', views.submit_marks, name='submit_marks'),
    
    path('submit_marks/<int:student_id>/<int:subject_id>/', views.submit_marks, name='submit_marks'),
    
    path('academic_marks/', views.academic_marks, name='academic_marks'),
    
    path('subject_marks/<int:subject_id>/', views.subject_marks_view, name='subject_marks_view'),
    
    path('get-subjects-for-day/', views.get_subjects_for_day, name='get_subjects_for_day'),
    
    
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('view_student_feedback/', views.view_student_feedback, name='view_student_feedback'),
    path('view_class_feedback/<int:class_id>/', views.view_class_feedback, name='view_class_feedback'),
    
    path('manage_feedback_questions/', views.manage_feedback_questions, name='manage_feedback_questions'),
    path('add_feedback_question/', views.add_feedback_question, name='add_feedback_question'),
    
    path('delete_feedback_question/<int:question_id>/', views.delete_feedback_question, name='delete_feedback_question'),
    path('feedback_student/', views.feedback_student, name='feedback_student'),
    
    path('view-feedback-students/', views.view_feedback_students, name='view_feedback_students'),
    path('feedback-details/<int:class_id>/', views.feedback_details, name='feedback_details'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)