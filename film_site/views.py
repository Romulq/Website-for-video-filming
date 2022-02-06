from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages

from .models import VideoType, MyWorks, AboutMe
from .forms import OrderForm


class HomeView(View):

    def get(self, request):

        types = VideoType.objects.all()
        works = MyWorks.objects.all()[:6]
        aboutMe = AboutMe.objects.first()
        
        context = {
            'types': types, 'works': works, 'aboutMe': aboutMe
        }

        return render(request, 'film_site/home.html', context)


class WorksView(View):

    def get(self, request):

        types = VideoType.objects.all()
        works = MyWorks.objects.all()            

        context = {
            'types': types, 'works': works
        }

        return render(request, 'film_site/works.html', context)


class CalcView(View):

    def post(self, request):

        form = OrderForm(request.POST or None)

        if form.is_valid():
            print("Success")
        
        type = VideoType.objects.get(id=form.data['typeVideo'])
        time = form.data['timeWork']
        result = int(type.price) * int(time)

        return JsonResponse({'data': result}, status=200)


class OrderView(View):

    def get(self, request):

        form = OrderForm(request.POST or None)

        context = {
            "form": form
        }

        return render(request, 'film_site/order.html', context)

    def post(self, request):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.firstName = form.cleaned_data['firstName']
            new_order.lastName = form.cleaned_data['lastName']
            new_order.eventDate = form.cleaned_data['eventDate']
            new_order.typeVideo = form.cleaned_data['typeVideo']
            new_order.timeWork = form.cleaned_data['timeWork']
            new_order.suggestions = form.cleaned_data['suggestions']
            new_order.phone = form.cleaned_data['phone']
            new_order.email = form.cleaned_data['email']
            new_order.save()

            type = VideoType.objects.get(id=form.data['typeVideo'])
            time = form.data['timeWork']
            new_order.price = int(type.price) * int(time)
            new_order.save()

            messages.add_message(request, messages.INFO, 'Спасибо за ваш заказ!')
            return HttpResponseRedirect('/')
        messages.add_message(request, messages.ERROR, 'Произошла ошибка! Попробуйте еще раз!')
        return HttpResponseRedirect('/order/')
