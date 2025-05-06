from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, StudentViewSet, ClassViewSet, ChargeClassPaymentView

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'classes', ClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('charge/', ChargeClassPaymentView.as_view()),
]
