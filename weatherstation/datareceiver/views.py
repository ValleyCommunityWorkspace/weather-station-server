from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from datetime import datetime

def decompress(raw):
    "Takes a bytes object with the compressed sensor data, returns list"

    # TODO finish me
    print("decompress got data: ", raw)

@csrf_exempt
@require_POST
def index(request):
    data = decompress(request.body)
    # TODO put data in database as appropriate

    # TODO Figure out an appropriate format for this
    correctedTime = str(datetime.now()).encode("UTF-8")
    return HttpResponse(b"Got it " + correctedTime)

