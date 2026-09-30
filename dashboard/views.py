from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Sum, Count
from django.db.models import F
from .serializers import LowStockAlert

# உங்கள் apps-ல் உள்ள models-ஐ import செய்து கொள்ளுங்கள்
from vehicles.models import Vehicle
from service.models import Service  # உங்கள் Service model பெயர்
from invoice.models import Invoice  # உங்கள் Invoice/Bill model பெயர்
from spareparts.models import SparePart
from .serializers import RecentServiceSerializer  

class DashboardSummaryView(APIView):
    def get(self, request):
        today = timezone.now().date()
        current_month = timezone.now().month
        current_year = timezone.now().year

        # 1. TOP CARDS (Metrics)
        total_vehicles = Vehicle.objects.count()
        active_repairs = Service.objects.filter(status='IN_PROGRESS').count()
        # ready_to_deliver = Service.objects.filter(status='READY').count()
        
        # நடப்பு மாத வருமானம் (Paid bills only)
        month_revenue = Invoice.objects.filter(
            payment_status='PAID',
            invoice_date__year=current_year,
            invoice_date__month=current_month
        ).aggregate(total=Sum('total_amount'))['total'] or 0

        # 2. RECENT 4-5 SERVICES (Recent Service Records Table)
        # # select_related போடுவதால் customer & vehicle data ஒரே query-ல் fast-ஆக fetch ஆகும்
        recent_services = Service.objects.select_related('vehicle').order_by('-created_at')[:5]
        recent_data = RecentServiceSerializer(recent_services, many=True).data

        # 3. SPARE PARTS ALERTS (Stock 5-க்கு குறைவாக உள்ளவை)
        low_stock_parts = SparePart.objects.filter(
            quantity__lte=F('minimum_stock')
        ).order_by('quantity')[:5]

        # 4. SERVICE TYPE DISTRIBUTION (Donut Chart-க்கான Data)
        service_types_breakdown = Service.objects.values('service_type').annotate(
            count=Count('id')
        ).order_by('-count')

        # FINAL JSON RESPONSE (React-க்கு தேவையான முழு payload)
        return Response({
            "metrics": {
                "total_vehicles": total_vehicles,
                "active_repairs": active_repairs,
                # "ready_to_deliver": ready_to_deliver,
                "month_revenue": month_revenue,
            },
            "recent_services": recent_data,
            "stock_alerts": LowStockAlert(low_stock_parts, many=True).data,
            "service_distribution": list(service_types_breakdown),
        })