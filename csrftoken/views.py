from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import logging

logger = logging.getLogger(__name__)

@csrf_protect
def custom_csrf_view(request):
    print("DID IT GET HERE???")
    if request.method == 'POST':
        logger.debug("POST request received")
        print("IS IT HERE???")
        return JsonResponse({'message': 'Resource created successfully'}, status=201)
    logger.debug("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=400)
