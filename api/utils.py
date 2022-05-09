from rest_framework.response import Response
from rest_framework import status

def check_auth(request):
    phone_number = request.data.get("phone_number")

    if not phone_number:
        return Response(
            {"detail": "Unauthorized request", "description": "The phone_number field is required"},
            status=status.HTTP_400_BAD_REQUEST
            )
    return phone_number