from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.product_offering import get_product_offerings

class ProductOfferingView(APIView):
    def get(self, request):
        try:
            data = get_product_offerings()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
