# @Author: andreacasino
# @Date:   2017-09-14T21:01:06+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-14T21:56:49+01:00

from rest_framework import serializers
from main.models import Palindrome

class PalindromeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palindrome
        fields = ('text',)

    def create(self,validated_data):
        return Palindrome.objects.create(**validated_data)
