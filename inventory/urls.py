from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductUpdateView
from . import views

urlpatterns = [
    path('product', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    #path('about/', views.about, name='blog-about'),
]
