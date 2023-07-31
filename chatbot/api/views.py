from ..chatbot_logic import get_response
from .serializers import ChatbotSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ChatbotView(APIView):

    def post(self, request, format=None):
        serializer = ChatbotSerializer(data=request.data)

        if serializer.is_valid():
            query = serializer.data.get('input_text')
            response = get_response(query)
            response = response.replace('\n', '<br>')
            return Response({"response": response})

        return Response(serializer.errors, status=400)