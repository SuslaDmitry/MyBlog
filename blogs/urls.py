from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница. Вывод всех публичных постов.
    url(r'^$', views.public_posts, name='index'),

    # Страница для добавления новой темы
    url(r'^new_post/$', views.new_post, name='new_post'),

    # Страница для редактирования записи
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,
    name='edit_post'),

    # Страница с личными публикациями
    url(r'^owner_posts/$', views.owner_posts, name='owner_posts'),
]
app_name = 'blogs'