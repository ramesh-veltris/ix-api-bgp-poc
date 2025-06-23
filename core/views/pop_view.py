from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.pop import get_pops

class PopView(APIView):
    def get(self, request):
        try:
            data = get_pops()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
