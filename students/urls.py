from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<username>\w+)/$', 'students.views.profile', name='profile'),
    url(r'^(?P<username>\w+)/edit/$', 'students.views.edit_student', name='edit_student'),
    url(r'^delete-student/$', 'students.views.delete_student', name='delete_student'),
    url(r'^create-student/$', 'students.views.create_student', name='create_student'),
]
