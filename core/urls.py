from django.urls import path
from core.views.product_offering_view import ProductOfferingView
from core.views.pop_view import PopView
from core.views.mac_view import MacView
from core.views.role_assignment_view import RoleAssignmentView
from core.views.connection_view import ConnectionView
from core.views.network_service_view import NetworkServiceView
from core.views.network_service_config_view import NetworkServiceConfigView
from core.views.network_feature_view import NetworkFeatureView
from core.views.network_feature_config_view import NetworkFeatureConfigView

urlpatterns = [
    path('product-offerings/', ProductOfferingView.as_view(), name='product-offerings'),
    path('pops/', PopView.as_view(), name='pops'),
    path('macs/', MacView.as_view(), name='macs'),
    path('role-assignments/', RoleAssignmentView.as_view(), name='role-assignments'),
    path('connections/', ConnectionView.as_view(), name='connections'),
    path('network-services/', NetworkServiceView.as_view(), name='network-services'),
    path('network-service-configs/', NetworkServiceConfigView.as_view(), name='network-service-configs'),
    path('network-features/', NetworkFeatureView.as_view(), name='network-features'),
    path('network-feature-configs/', NetworkFeatureConfigView.as_view(), name='network-feature-configs'),
]
