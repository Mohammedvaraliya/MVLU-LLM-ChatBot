from rest_framework import serializers

class ChatbotSerializer(serializers.Serializer):
    input_text = serializers.CharField()