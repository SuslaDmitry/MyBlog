from django.conf.urls import path, re_path
from django.urls import path, re_path
from . import views

urlpatterns = [
    # Домашняя страница. Вывод всех публичных постов.
    re_path(r'^$', views.public_posts,
        name='index'),

    # Страница для добавления нового поста
    re_path(r'^new_post/$', views.new_post,
        name='new_post'),

    # Страница для редактирования записи
    re_path(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,
        name='edit_post'),

    # Удаление поста
    re_path(r'^delete_post/(?P<post_id>\d+)/$', views.delete_post,
        name='delete_post'),

    # Страница с личными публикациями
    re_path(r'^owner_posts/$', views.owner_posts,
        name='owner_posts'),

    # Страница для отельного поста
    re_path(r'^post_details/(?P<post_id>\d+)/$', views.post_details,
        name='post_details'),

    # Публикация/приватизация поста
    re_path(r'^privat_public/(?P<post_id>\d+)/$', views.privat_public,
        name='privat_public'),

    # Страница для добавления нового tag
    re_path(r'^new_tag/$', views.new_tag,
        name='new_tag'),

    # Введет все посты, прикрепленные к этому тегу
    re_path(r'^tag_detail/(?P<tag_id>\d+)/$', views.tag_detail, name='tag_detail'),

    # Удаление поста
    re_path(r'^delete_tag/(?P<tag_id>\d+)/$', views.delete_tag,
        name='delete_tag'),

]
app_name = 'blogs'
