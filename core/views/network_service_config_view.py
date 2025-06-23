from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.network_service_config import get_network_service_configs, create_network_service_config

class NetworkServiceConfigView(APIView):
    def get(self, request):
        try:
            data = get_network_service_configs()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            result = create_network_service_config(request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
