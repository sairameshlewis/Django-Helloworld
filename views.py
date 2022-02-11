
from django.http import JsonResponse

# Create your views here.

def show(request):
    data = {"Message":"Hello World"}
    return JsonResponse(data)
    
