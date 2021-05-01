from django.http import JsonResponse

# Create your views here.
def produtos(request):
    if request.method == 'GET':
        p = {
            'id': 1,
            'nome': 'Lucas'
        }
        return JsonResponse(p)