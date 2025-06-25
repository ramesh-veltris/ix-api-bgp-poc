from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.accounts import get_accounts, create_account

class AccountListView(APIView):
    def get(self, request):
        try:
            data = get_accounts()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            result = create_account(request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
