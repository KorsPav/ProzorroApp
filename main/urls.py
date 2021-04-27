from django.urls import path, include
from main.views import TenderSearchView


urlpatterns = [
    path('', TenderSearchView.as_view(), name='tender_search'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]