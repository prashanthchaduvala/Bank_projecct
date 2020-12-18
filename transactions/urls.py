from django.urls import re_path

from .views import deposit_view, withdrawal_view


app_name = 'transactions'
urlpatterns = [
    # url(r'^$', home_view, name='home'),
    re_path('deposit/', deposit_view, name='deposit'),
    re_path('withdrawal/', withdrawal_view, name='withdrawal'),
]
