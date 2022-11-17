from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.
# def index(request: HttpRequest) -> HttpResponse:
#     return HttpResponse('<h1>Hello world!</h1><br><h2>Hello world!</h2><br><h3>Hello world!</h3>')
#
# def jsonify(request: HttpRequest) -> HttpResponse:
#     return JsonResponse({"data": 1})
#
# def rendering(request: HttpRequest) -> HttpResponse:
#     return render(request, 'base.html', context={"data": 10})


# Новое
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user_app/signup.html'
