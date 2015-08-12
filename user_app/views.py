from django.shortcuts import render_to_response

# Create your views here.

def test(request):
    return render_to_response('test.html')