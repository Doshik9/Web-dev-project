from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Work, Assessment
from .forms import WorkForm

# Create your views here.
class WorkListView(ListView):
    model = Work
    paginate_by = 1
    # Дальше только для удобства
    template_name = 'education_app/works_list.html'
    context_object_name = "works"


class WorkDetailView(DetailView):
    model = Work
    # Дальше только для удобства
    template_name = 'education_app/works_detail.html'
    context_object_name = "work"
    pk_url_kwarg = 'id'


class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works-list')
    # Для удобства
    template_name_suffix = '_create'


class WorkDeleteView(DeleteView):
    model = Work
    success_url = reverse_lazy('works-list')
    # Для удобства
    template_name_suffix = '_delete'
    pk_url_kwarg = 'id'


class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('works-list')
    # Для удобства
    template_name_suffix = '_update'
    pk_url_kwarg = 'id'


# class WorkListView(View):
#     template_name = 'education_app/works_list.html'
#     form_class = WorkForm
#
#     def __get_context(self, **kwargs: dict) -> dict:
#         works = Work.objects.all()
#         form = self.form_class()
#         return {'works': works, 'form': form} | kwargs
#
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return render(request, self.template_name, context=self.__get_context())
#
#     def post(self, request: HttpRequest) -> HttpResponse:
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#
#         return render(request, self.template_name, context=self.__get_context())


# class WorkDetailView(View):
#     template_name = 'education_app/works_detail.html'
#     form_class = WorkForm
#
#     def __get_context(self, work: Work, **kwargs: dict) -> dict:
#         form = self.form_class(instance=work)
#         return {'work': work, 'form': form} | kwargs
#
#     def get(self, request: HttpRequest, id: int) -> HttpResponse:
#         work = get_object_or_404(Work, id=id)
#         return render(request, self.template_name, context=self.__get_context(work=work))
#
#     def post(self, request: HttpRequest, id: int) -> HttpResponse:
#         work = get_object_or_404(Work, id=id)
#         form = WorkForm(request.POST, instance=work)
#         if form.is_valid():
#             form.save()
#
#         return render(request, self.template_name, context=self.__get_context(work=work))


# def work_list(request: HttpRequest) -> HttpResponse:
#     works = Work.objects.all()
#
#     if request.method == 'POST':
#         form = WorkForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     # Просто очистка формы, чтобы убрать данные прошлого объекта
#     form = WorkForm()
#
#     context={
#         'works': works,
#         'form': form,
#     }
#
#     return render(request, 'education_app/works_list.html', context=context)


# def work_detail(request: HttpRequest, id: int) -> HttpResponse:
#     work = get_object_or_404(Work, id=id)
#
#     if request.method == 'POST':
#         form = WorkForm(request.POST, instance=work)
#         if form.is_valid():
#             form.save()
#
#     form = WorkForm(instance=work)
#
#     context = {
#         'work': work,
#         'form': form,
#     }
#
#     return render(request, 'education_app/works_detail.html', context=context)