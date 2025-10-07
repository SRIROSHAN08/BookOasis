from django.shortcuts import render
from .forms import *
from .models import *
from django.views import View
from django.views.generic.detail import DetailView
# Create your views here.
class AllContribView(View):
    def get(self,request):
        context={
            'all_bookers':BookersDetails.objects.all()
        }
        
        return render(request,'booker.html',context)

class BookerDetailView(DetailView):
    model= BookersDetails
    template_name='booker_detail.html'
    context_object_name='contributor'
    