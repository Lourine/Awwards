from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'project/post/$',views.post,name='post'),
    url(r'^user/profile/$',views.profile,name='profile'),
    url(r'^project/(\d+)/',views.project_detail,name='details'),
    url(r'^search/projects/results/$',views.search,name="search"),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^developer/api/$',views.apiView,name='api'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
