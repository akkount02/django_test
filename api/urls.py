from rest_framework.routers import DefaultRouter

import api.views as views

router = DefaultRouter()
router.register(r"product", views.ProductModelView)

urlpatterns = router.urls
