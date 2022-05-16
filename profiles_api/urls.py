from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, basename='Hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('medicamentos',views.MedicamentosViewSet )
urlpatterns = [
    path('hello-view', views.HelloApi.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

