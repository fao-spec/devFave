from django.urls import path
from web.views import home
from web.views import profile
from web.views import student
from web.views import newstudent


urlpatterns = [
    path('', home, name='home'),
    # path('<profile>', profile),
    path('students', student,),
    path('new_student', newstudent, name = 'newstudents')
]