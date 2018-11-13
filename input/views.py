from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from urlG import get_url_from_points
from url_to_img_tag import annotate_urls

def index(request):

    context = {}
    return render(request, 'input/index.html', context)


def geturl(request):
    # it is text input
    start_latitude = float(request.GET.get('start_latitude'))
    start_longitude = float(request.GET.get('start_longitude'))
    end_latitude = float(request.GET.get('end_latitude'))
    end_longitude = float( request.GET.get('end_longitude'))
    N = request.GET.get('N')

    # print("-------------")
    # print((start_latitude, start_longitude))
    # print((end_latitude, end_longitude))
    # print(type(start_latitude))
    # start = (42.348933, -71.097594)
    # end = (42.352140, -71.123463)
    urls = get_url_from_points((start_latitude, start_longitude), (end_latitude, end_longitude), N)


    # annotate_urls(urls)


    with open('result.csv', 'r') as f:
        f = [x.strip('\n') for x in f][1:]
        f = [x.split(',') for x in f]

        return render(request, 'input/result.html', {
            'result_list': f,
        })

