from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from order.forms import AddToCartForm
from product.forms import ProductForm, ProductImageForm
from product.models import Product, Category, ProductImage


# CRUD(Create, Retrieve, Update, Delete)
# TODO: реализовать CRUD
# TODO: авторизация
# TODO: реализовать проверку прав пользователя

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products_list.html'
    context_object_name = 'products'


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart-form'] = AddToCartForm()
        return context


ImagesFormSet = modelformset_factory(ProductImage,
                                             form=ProductImageForm,
                                             extra=3,
                                             max_num=5,
                                             can_delete=True)


# TODO: реализовать при помощи функции
#TODO: создание, редактирование и удаление продуктов могли делать только администраторы

class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_staff




class CreateProductView(UserPassesTestMixin, CreateView):
    queryset = Product.objects.all()
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-list')

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('product-image'):
                ProductImage.objects.create(product=product, image=image)
            return redirect(reverse_lazy('product-details', args=(product.id, )))
        return self.form_invalid(form)


class UpdateProductView(UserPassesTestMixin, UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'product'


class DeleteProductView(UserPassesTestMixin, DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('products-list')


class IndexPageView(TemplateView):
    template_name = 'product/index.html'





# CRUD(Create, Retrieve, Update, Delete)



# MVC(Model-View-Controller)
#
# Model           (models)
# View            (template)
# Controller      (view)



# request  -->  Controller
# response <-------|
#
#   View          Controller    <---->   Model  <--->    Data Base
#             /        \
#            /          \
# request ->             -> response

