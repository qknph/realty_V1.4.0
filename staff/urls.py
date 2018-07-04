
from django.conf.urls import url

from staff import views

urlpatterns = [
    url(r'^emp_list.html', views.emp_list),
    url(r'^house_list.html', views.house_list),
    url(r'house_type_list.html', views.house_type_list),
    url(r'dept_list.html', views.dept_list),
    url(r'notice_list.html', views.notice_list),
    url(r'^delete/',views.house_type_delete),
    url(r'^d_delete/',views.d_del_view),
    url(r'^E_del/',views.E_del_view),
    url(r'^Edit/',views.Ed_view),
    url(r'^query_house/',views.query_house),
    url(r'^query_house_type/',views.query_house_type),
    url(r'^query_dept/',views.query_dept),
    url(r'^note_del/',views.note_del),
    url(r'^query_note/',views.query_note)




]