from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class ProductListView(ListView):
    # queryset = Product.objects.filter(active=True).order_by('-datetime_created')[:100]
    queryset = Product.active_objects.all().order_by('-datetime_created').order_by('-price')
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def form_valid(self, form):  # new
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    success_message = "نظر شما با موفقیت ثبت شد"

    def form_valid(self, form):  # new

        obj = form.save(commit=False)
        obj.user = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)
