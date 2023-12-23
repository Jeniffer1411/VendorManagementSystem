from django.urls import path
from .views import VendorApi, PurchaseOrderApi, vendorPerformance, purchaseOrderAcknowledged

urlpatterns = [
    path('vendors/', VendorApi.as_view()),
    path('vendors/<int:vendor_id>/', VendorApi.as_view()),
    path('purchase_orders/', PurchaseOrderApi.as_view()),
    path('purchase_orders/<str:po_number>/', PurchaseOrderApi.as_view()),
    path('vendors/<int:vendor_id>/performance/', vendorPerformance),
    path('purchase_orders/<str:po_number>/acknowledge/', purchaseOrderAcknowledged)
]





