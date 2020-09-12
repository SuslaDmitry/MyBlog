from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница. Вывод всех публичных постов.
    url(r'^$', views.public_posts,
        name='index'),

    # Страница для добавления нового поста
    url(r'^new_post/$', views.new_post,
        name='new_post'),

    # Страница для редактирования записи
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,
        name='edit_post'),

    # Удаление поста
    url(r'^delete_post/(?P<post_id>\d+)/$', views.delete_post,
        name='delete_post'),

    # Страница с личными публикациями
    url(r'^owner_posts/$', views.owner_posts,
        name='owner_posts'),

    # Страница для отельного поста
    url(r'^post_details/(?P<post_id>\d+)/$', views.post_details,
        name='post_details'),

    # Публикация/приватизация поста
    url(r'^privat_public/(?P<post_id>\d+)/$', views.privat_public,
        name='privat_public'),

]
app_name = 'blogs'
