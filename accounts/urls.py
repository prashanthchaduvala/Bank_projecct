from django.conf.urls import url


from .views import (
    login_view,
    register_view,
    logout_view
)

app_name = 'accounts'

urlpatterns = [
    url('login/', login_view, name='login'),
    url('register/', register_view, name='register'),
    url('logout/', logout_view, name='logout'),
]
