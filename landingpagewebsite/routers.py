from rest_framework.routers import DefaultRouter, SimpleRouter
from crm.views import OrderViewSet, CommentCrmViewSet, StatusCrmViewSet
from cms.views import CmsSliderViewSet
from price.views import PriceCardViewSet, PriceTableViewSet
from telebot.views import TeleSettingsViewSet
from authentication.views import UserViewSet


router = DefaultRouter()
simrouter = SimpleRouter()

router.register('order', OrderViewSet)
router.register('status', StatusCrmViewSet)
router.register('comment', CommentCrmViewSet)
simrouter.register('order', OrderViewSet)

router.register('slider', CmsSliderViewSet)

router.register('card', PriceCardViewSet)
router.register('table', PriceTableViewSet)

router.register('telegram', TeleSettingsViewSet)

router.register('auth', UserViewSet)
