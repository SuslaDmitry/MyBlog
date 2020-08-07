from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница. Вывод всех постов.
    url(r'^$', views.posts, name='index'),

    # Страница для добавления новой темы
    url(r'^new_post/$', views.new_post, name='new_post'),

    # Страница для редактирования записи
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,
    name='edit_post'),
]
app_name = 'blogs'