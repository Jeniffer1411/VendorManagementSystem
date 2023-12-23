from datetime import timedelta, datetime
from django.db.models import Count, Avg, F



def calculate_on_time_delivery_rate(vendor):
    from .models import PurchaseOrder
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    on_time_deliveries = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        delivery_date__lte=F('acknowledgment_date')
    ).count()

    if completed_orders > 0:
        on_time_delivery_rate = (on_time_deliveries / completed_orders) * 100
    else:
        on_time_delivery_rate = 0.0

    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor):
    from .models import PurchaseOrder
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

    return quality_rating_avg

def calculate_average_response_time(vendor):
    from .models import PurchaseOrder
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = [po.acknowledgment_date - po.issue_date for po in acknowledged_orders]
    
    if response_times:
        average_response_time = sum(response_times, timedelta()) / len(response_times)
    else:
        average_response_time = timedelta(seconds=0)

    average_response = average_response_time.total_seconds() / 60.0   # Convert to minutes
    return round(average_response, 3)   
   
def calculate_fulfillment_rate(vendor):
    from .models import PurchaseOrder
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

    if total_orders > 0:
        fulfillment_rate = (fulfilled_orders / total_orders) * 100
    else:
        fulfillment_rate = 0.0

    return fulfillment_rate

def update_vendor_performance_metrics(vendor):
    from .models import HistoricalPerformance, PurchaseOrder
    if vendor!=None:
        # Calculate metrics
        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        quality_rating_avg = calculate_quality_rating_avg(vendor)
        average_response_time = calculate_average_response_time(vendor)
        fulfillment_rate = calculate_fulfillment_rate(vendor)

        # Update vendor model
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        # Optionally, store historical performance
        HistoricalPerformance.objects.create(
            vendor=vendor,
            date = datetime.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )
    else: 
        raise VendorPerformanceUpdateError("Vendor Not Found to Update Performance")

class VendorPerformanceUpdateError(Exception):
    pass

def updateResponseTime(vendor):
    if vendor!=None:
        average_response_time = calculate_average_response_time(vendor)
        vendor.average_response_time = average_response_time
