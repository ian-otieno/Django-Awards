from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search/', views.search, name='search'),
    url(r'^project/(\d+)/$',views.project_detail,name ='project_detail'),
    url(r'^new/project', views.new_project, name='new-project'),
    path('delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),
    path('rating/<int:project_id>', views.rating, name='rating'),
    url(r'^api/v3/project/$', views.ProjectList.as_view()),
    url(r'^api/v3/profile$', views.ProfileList.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
