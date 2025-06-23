from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.services.role_assignment import get_role_assignments, create_role_assignment

class RoleAssignmentView(APIView):
    def get(self, request):
        try:
            data = get_role_assignments()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            result = create_role_assignment(request.data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
