from django.shortcuts import render
from Blog import settings
from .forms import *
from .models import *
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
# Create your views here.



# def Book_add(request):
    
#     context={
#         'book_form':BookDetails_Form()
#     }
    
#     if request.method == "POST":
#         book_form=BookDetails_Form(request.POST)
        
#         if book_form.is_valid():
#             book_form.save()
#             return redirect('/post/book/')
                    
#     return render(request,'book_add.html',context)


# def AllBooks(request):
#     context={
#         'all_books':BookDetails.objects.all()
#     }
    
#     return render(request,'books.html',context)


# def DeleteBooks(request,id):
    
#     selected_book=BookDetails.objects.get(id = id)
    
#     selected_book.delete()
    
#     return redirect('/post/book/')
    

# def BookUpdate(request,id):
    
#     selected_book=BookDetails.objects.get(id = id)
    
#     context={
#         'book_form' : BookDetails_Form(instance=selected_book)
#     }
    
#     if request.method=="POST":
#         book_form=BookDetails_Form(request.POST,instance=selected_book)
        
#         if book_form.is_valid():
#             book_form.save()
#             return redirect('/post/book/')
    
#     return render(request,'book_add.html',context)


class AllBooksView(View):
    
    def get(self,request):
        context={
        'all_books':BookDetails.objects.all()
        }
    
        return render(request,'books.html',context)


class BookDetailView(DetailView):
    model=BookDetails
    template_name='book_detail.html'
    context_object_name='book'

class WeatherView(TemplateView):
    template_name = 'weather.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_key = settings.api_key
        city = self.request.GET.get('city','Chennai')
        url =  f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 :
            weather = {
                'city' :city,
                'temperature' : data['main']['temp'],
                'description' : data['weather'][0]['description'],
                'humidity' : data['main']['humidity'],
            }
        else:
            weather = None
            
        context['weather'] = weather
        return context