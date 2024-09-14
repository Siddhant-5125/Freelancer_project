from django.urls import path

from .views import index, FreeLancerListView, FreeLancerDetailView, FreeLancerCreateView, BusinessListView, BusinessCreateView, handle_login, BusinessDetailView, Home

urlpatterns = [
    path('', Home, name='home'),
    path('account-setup/', handle_login, name='handle-login'),
    path('developer/list/', FreeLancerListView.as_view(), name='freelancer-list'),
    path('business/list/', BusinessListView.as_view(), name='business-list'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('developer/<int:pk>/', FreeLancerDetailView.as_view(), name='freelancer-detail'),
    path('developer/create/', FreeLancerCreateView.as_view(), name='freelancer-create'),
    path('business/create/',  BusinessCreateView.as_view(), name='business-create'),
]