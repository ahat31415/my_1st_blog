from django.conf.urls import url  # импорт url функции джанго
from . import views  # импортируем все представления из приложения blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^2h$', views.post_list_2h, name='post_list_2h'),


    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^delete_post/(?P<pk>\d+)$', views.delete_post, name='delete_post'),
    url(r'^delete_posts', views.delete_posts, name='delete_posts'),
    url(r'^adding_posts$', views.adding_posts, name='adding_posts'),

]
