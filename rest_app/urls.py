
from django.urls import path
from .views import *

urlpatterns = [
    path('location/', LocationListCreateAPIView.as_view(), name='location-list-create'),
    path('location/<int:pk>/', LocationDetailAPIView.as_view(), name='location-detail'),
    path('location/<int:location_id>/department/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('location/<int:location_id>/department/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('location/<int:location_id>/department/<int:department_id>/category/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/', SubcategoryListCreateAPIView.as_view(), name='subcategory-list-create'),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/<int:pk>/', SubcategoryDetailAPIView.as_view(), name='subcategory-detail'),
    path('sku/match/', search_sku_by_metadata, name='sku-match'),
]
