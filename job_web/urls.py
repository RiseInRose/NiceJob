from job_web.views import index2,mine,helps,ajax_test
from job_web.views import my_vitae,auto_launch_vitae,message_board
from job_web.views import contact
from django.conf.urls import url

urlpatterns = [
    url(r'^index/', index2),
    url(r'^help/', helps),
    url(r'^mine/', mine),
    url(r'^contact/', contact),
    url(r'^my_vitae/', my_vitae),
    url(r'^auto_launch_vitae/', auto_launch_vitae),
    url(r'^message_board', message_board),
    url(r'^ajax_test', ajax_test),

]