
from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,ItemImage
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import AddItem
from .filters import ItemFilter
# Create your views here.

def product(request):
    product = Item.objects.all()

    #Filter
    myfilter = ItemFilter(request.GET , queryset=product)
    product = myfilter.qs

    #paginator
    paginator = Paginator(product,12)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)


    context = {'pro':page_object,'myfilter':myfilter}
    return render(request,'product/products.html',context)

@login_required
def add_item(request):

    if request.method=='POST':
        form = AddItem(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:product'))

    else :
        form = AddItem()

    context = {'form':form}
    return render(request,'product/add_product.html',context)   

@login_required
def product_detail(request,slug):
    product_detail = Item.objects.get(slug=slug)
    # product_detail = get_object_or_404(Item,slug=slug)
    context = {'pro':product_detail}
    return render(request,'product/product_detail.html',context)