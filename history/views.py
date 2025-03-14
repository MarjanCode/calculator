from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import HistorySerializer
from .models import History
import re



class HistoryAPIView(APIView):
    def post(self, request):
        equation = request.data.get('equation')

        if not equation or not equation.strip():
            return Response(
                {"error": "Equation cannot be empty or null."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not re.match(r'^[\d+\-*/(). =]+$', equation):
            return Response(
                {"error": "Invalid characters in the equation."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        history = History.objects.all().order_by('-id')[:10]
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)