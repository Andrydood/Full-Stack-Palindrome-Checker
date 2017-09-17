# @Author: andreacasino
# @Date:   2017-09-14T19:03:34+01:00
# @Last modified by:   andreacasino
# @Last modified time: 2017-09-17T19:06:27+01:00

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Palindrome
from main.serializers import PalindromeSerializer
from main.functions import isPalindrome


@csrf_exempt
def palindrome_contact(request):

    if request.method == 'GET':
        #Only consider the latest 100 objects
        palindrome = Palindrome.objects.all()[:100]
        serializer = PalindromeSerializer(palindrome,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PalindromeSerializer(data=data)
        if serializer.is_valid():
                if isPalindrome(serializer.validated_data['text']):
                    serializer.save()
                    return JsonResponse(True,status=201,safe=False)
                return JsonResponse(False,status=200,safe=False)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        palindrome = Palindrome.objects.all()
        palindrome.delete()
        return HttpResponse(status=204)

@csrf_exempt
def page(request,page):
    page = int(page)

    if request.method == 'GET':
        #Only consider the 10 objects in the given page
        palindrome = Palindrome.objects.all()[:100]
        palindromePage = palindrome[page*10:page*10+10]
        serializer = PalindromeSerializer(palindromePage,many=True)
        return JsonResponse(serializer.data,safe=False)
