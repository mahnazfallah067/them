import itertools

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from shop_order.forms import UserNewOrderForm
from .models import Product
from django.views.generic import ListView, DetailView
from shop_category.models import Category
from django.http import Http404
from shop_comment.models import Comment
from .forms import AddCommentForm

# Create your views here.


class ProductList(ListView):
    template_name = 'product/products.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductCategory(ListView):
    template_name = 'product/products.html'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('دسته بندی موردنظر یافت نشد')
        return Product.objects.get_product_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, id, *args, **kwargs):


    product = Product.objects.get(id=id)
    selected_product_id = kwargs['productId']
    product_name = kwargs['name']

    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})

    product: Product = Product.objects.get_by_id(selected_product_id)

    if product is None:
        raise Http404
    comments = Comment.objects.filter(product=product, is_reply=False)
    related_products = Product.objects.get_queryset().filter(category__product=product).distinct()
    grouped_related_products = my_grouper(4, related_products)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            return redirect('/')

    else:
       form = AddCommentForm()

    context = {
        'product': product,
        'comments': comments,
        'related_products': grouped_related_products,
        'form': form,
        'new_order_form': new_order_form,

    }
    return render(request, 'product/product_detail.html', context)


class SearchResultsView(ListView):
    template_name = 'product/products.html'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        return object_list












