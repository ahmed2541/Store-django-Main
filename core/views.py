
from django.shortcuts import render
from product.models import Item
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    product = Item.objects.all()

    paginator = Paginator(product,8)  
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)


    context = {'pro':page_object}
    return render(request,'core/home.html',context)