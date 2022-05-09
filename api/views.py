from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SellsPoint, Visit, Worker
from .serializers import SellsPointSerializer
from django.core.exceptions import ObjectDoesNotExist

class SellPointsView(APIView):
    def get(self, request):
        phone_number = request.data.get("phone_number")

        if not phone_number:
            return Response(
                {"detail": "Unauthorized request", "description": "The phone_number field is required"},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        try:
            worker = Worker.objects.get(phone_number=phone_number)
        except ObjectDoesNotExist:
            return Response({"detail": f"No worker found with phone_number {phone_number}"}, status=status.HTTP_404_NOT_FOUND)

        queryset = SellsPoint.objects.filter(worker_id=worker.id)

        sell_points = SellsPointSerializer(queryset, many=True)

        return Response(sell_points.data, status=status.HTTP_200_OK)
    
class VisitView(APIView):
    def post(self, request):
        pk = request.data.get("sells_point_id")
        lon = request.data.get("longitude")
        lat = request.data.get("latitude")
        phone_number = request.data.get("phone_number")

        if not phone_number:
            return Response(
                {"detail": "Unauthorized request", "description": "The phone_number field is required"},
                status=status.HTTP_400_BAD_REQUEST
                )

        if not pk:
            return Response(
                {"detail": "Sells point id is required"},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if not lon:
            return Response(
                {"detail": "Longitude is required"},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if not lat:
            return Response(
                {"detail": "Latitude is required"},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        try:
            sells_point = SellsPoint.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"detail": f"No sells point found with id {pk}"}, status=status.HTTP_404_NOT_FOUND)
        
        if phone_number == sells_point.get_worker_phone_number():
            visit = Visit(longitude=lon, latitude=lat, sells_point=sells_point)
            visit.save()
            return Response({"time": visit.time, "id": visit.pk}, status=status.HTTP_201_CREATED)

        return Response(
            {"detail": "Unauthorized request"},
            status=status.HTTP_400_BAD_REQUEST
            )