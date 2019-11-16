from django.urls import path
from product_app import views
urlpatterns = [
    path('SpCategory/', views.SpCategoryAPIView.as_view(), name="sp-category"),
    path('SpSubCategory/', views.SpSubCategoryAPIView.as_view(), name="sp-sub-category"),
    path('SpProduct/', views.SpProductAPIView.as_view(), name="sp-product"),
    path('SpDivision/', views.SpDivisionAPIView.as_view(), name="sp-division"),

    path('sp-category-detail/<int:pk>/', views.SpCategoryDetail.as_view()),
    path('sp-category-list/', views.SpCategoryList.as_view()),
    path('sp-sub-category-detail/<int:pk>/', views.SpSubCategoryDetail.as_view()),
    path('sp-sub-category-list/', views.SpSubCategoryList.as_view()),
    path('sp-product-detail/<int:pk>/', views.SpProductDetail.as_view()),
    path('sp-product-detail-list/', views.SpProductList.as_view()),
    path('sp-division-detail/<int:pk>/', views.SpDivisionDetail.as_view()),
    path('sp-division-list/', views.SpDivisionList.as_view()),

]