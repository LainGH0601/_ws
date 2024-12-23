from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        images = request.FILES['images']
        print(type(images))
        handle_uploaded_file(images)
        print(len(request.FILES))
        print(type(request.FILES))
        print(len(request.FILES))
        for f in request.FILES:
            print(type(f))
            print(f)
        #handle_uploaded_file(images[1])
        return HttpResponse(200)
    return HttpResponse(404)



def handle_uploaded_file(f):
    destination = open('test.jpg', 'wb')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()