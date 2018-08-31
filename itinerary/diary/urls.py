from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	#主页
	url(r'^topics/$', views.topics, name = 'topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),	
	url(r'new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	url(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
	#url(r'^edit_topic/$', views.edit_topic, name = 'edit_topic')
	url(r'^showImg/$', views.showImg, name = 'showImg'),
	url(r'^uploadImg/$', views.uploadImg, name = 'uploadImg'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)