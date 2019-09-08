from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'login', views.Login,basename='Login')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('login', views.Login.as_view(), name="logins"),
]
