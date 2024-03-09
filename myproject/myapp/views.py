from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from myapp.forms import AddProductForm, CommentForm
from myapp.models import Comment, Favorite, Product
from myapp.utils import DataMixin


# Create your views here.
class HomeView(DataMixin, ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data()
        c_def = self.get_user_context(title='Лента')
        return dict(list(c_def.items())+list(context.items()))

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('initiator')


class Tags(DataMixin, ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs['tag_slug']).prefetch_related('initiator')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Tags, self).get_context_data()
        c_def = self.get_user_context(title='Лента')
        return dict(list(c_def.items())+list(context.items()))


def chat(request):
    return render(request, 'myapp/chat.html')


class AddProduct(DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'myapp/add_product.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AddProduct, self).get_context_data()
        c_def = self.get_user_context(title='Добавление поста')
        return dict(list(c_def.items())+list(context.items()))

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(AddProduct, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('home')


def comment_add(request, product_id):
    product = Product.objects.get(id=product_id)
    comment = Comment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.product = product
            form.save()
            return redirect(comment_add, product_id)
    else:
        form = CommentForm()

    return render(request, 'myapp/comments.html', {
        'form': form,
        'product': product,
        'comment': comment,
    })


def favorite_add(request, product_id):
    product = Product.objects.get(id=product_id)
    favorite = Favorite.objects.filter(user=request.user, product=product)

    if not favorite.exists():
        Favorite.objects.create(user=request.user, product=product)
    else:
        favorite = favorite.first()
        favorite.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favorite_delete(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class Favorites(DataMixin, ListView):
    model = Favorite
    template_name = 'myapp/favorite.html'
    context_object_name = 'favorites'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Favorites, self).get_context_data()
        c_def = self.get_user_context(title='Избранные видео')
        return dict(list(c_def.items())+list(context.items()))

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
