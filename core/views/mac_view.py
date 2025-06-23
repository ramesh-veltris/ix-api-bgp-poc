from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.mac import get_macs, create_mac

class MacView(APIView):
    def get(self, request):
        try:
            data = get_macs()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            result = create_mac(request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
