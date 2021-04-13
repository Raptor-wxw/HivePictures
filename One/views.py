from django.http import HttpResponse
from django.shortcuts import render, redirect
from One.methods import suggest, images
from One.methods import get_video


# Create your views here.
from One.models import Pics, Pic


def index(request):
    context = images.images()
    return render(request, 'index.html', context=locals()['context'])


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        suggest.about(email, name, message)
        if name and email and message:
            context = {"alert": "<script>alert('您的建议我们已收到，我们很快会回复您')</script>"}
            return render(request, 'about.html', context=context)
        else:
            context = {"alert": "<script>alert('请确认您已完整填写所有内容')</script>"}
            return render(request, 'about.html', context=context)


def show(request):
    context = images.show()
    return render(request, 'show.html', context=locals()['context'])


def suggestion(request):
    return redirect('/about/#contact')


def register(request):
    return render(request, 'register.html')


def login(request):
    images.images()
    return render(request, 'login.html')


def video(request):
    url, where, where_id = get_video.video()
    if not (url and where and where_id):
        return render(request, 'video_error.html')
    else:
        context = {'video': url, 'where': where, 'id': where_id}
        return render(request, 'video.html', context=context)


def image(request):
    context = images.images()
    return render(request, 'images.html', context=context)


def picture(request, package):
    pics = Pics.objects.filter(package=package)
    text = Pic.objects.get(package=package).text
    return render(request, 'package_img.html', context=locals())


def search(request, wd):
    pics = ''
    word = ''
    if request.method == 'GET':
        word = wd
        pics = images.search(word)

    elif request.method == 'POST':
        word = request.POST.get('query')
        pics = images.search(word)
    if pics:
        text = '这是对“%s”的搜索结果' % word
    else:
        text = '抱歉未搜索到任何内容'
    return render(request, 'search.html', context=locals())
