from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from Calendar.models import Event
from Clients.forms import ProductForm, OrderForm, OrderLineForm
from Clients.models import Order, Customer, Product, Category, TextBox, OrderLine

        ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOMER
from Clients.render import Render


@login_required
def CustomersListView(request):
    customers = Customer.objects.all()
    return render(request, "customer/customers_list.html", {"customers": customers})


class CustomerAddView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone', 'e_mail', 'address', 'city', 'company', 'zip', 'status', 'website']
    template_name = 'customer/add_customer.html'
    success_url = '/customers_list/'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone', 'e_mail', 'address', 'city', 'company', 'zip','website']
    template_name = 'customer/edit_customer.html'
    success_url = '/customers_list/'


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    permission_required = ('delete_customer',)

    fields = ['first_name', 'last_name', 'phone', 'e_mail', 'address', 'city', 'company', 'zip','website']
    template_name = 'customer/delete_customer.html'
    success_url = '/customers_list/'

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRODUCT


@login_required
def ProductsListView(request):
    products = Product.objects.all().order_by('-product_stock')
    categories = Category.objects.all()
    return render(request, "product/products_list.html", {"products": products, "categories": categories})


class ProductAddView(LoginRequiredMixin, CreateView):
    model = Product
    form = ProductForm()
    fields = ['product_name', 'product_price', 'product_stock', 'category']
    template_name = 'product/add_product.html'
    success_url = '/products_list/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['product_name', 'product_price', 'product_stock', 'category']
    template_name = 'product/edit_product.html'
    success_url = '/products_list/'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = ('delete_product',)

    fields = ['product_name', 'product_price', 'product_stock', 'category']
    template_name = 'product/delete_product.html'
    success_url = '/products_list/'

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDER


@login_required
def OrdersListView(request):
    orders = Order.objects.all().order_by('-date')
    return render(request, "order/orders_list.html", {"orders": orders})


class OrderAddView(LoginRequiredMixin, CreateView):
    model = Order
    form = OrderForm()
    fields = ['customer_id', 'tax', 'invoices_days', 'status']
    template_name = 'order/add_order.html'
    success_url = '/orders/'

class OrderEditView(LoginRequiredMixin, UpdateView):
    model = Order
    form = OrderForm()
    fields = ['customer_id', 'tax', 'invoices_days', 'status']
    template_name = 'order/edit_order.html'
    success_url = '/orders/'

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ORDER LINE


class OrderAddLinesView(LoginRequiredMixin, View):
    def get(self, request, id):
        order = Order.objects.get(id=id)
        form = OrderLineForm()
        lines = OrderLine.objects.filter(order_id_id=id)
        order_value_dic = OrderLine.objects.filter(order_id_id=id).aggregate(Sum('total'))
        tax = order.get_tax_display()
        try:
            order_net_value = float(order_value_dic['total__sum'])
            order_gross_value = order_net_value * (1 + tax)
        except TypeError:
            order_net_value = 0.0
            order_gross_value = 0.0
        return render(request, 'order/addorderlines.html',
                      {'order': order, 'form': form, 'lines': lines, "order_net_value": order_net_value,
                       "order_gross_value": order_gross_value})

    def post(self, request, id):
        form = OrderLineForm(request.POST)
        order = Order.objects.get(id=id)
        tax = order.get_tax_display()
        if form.is_valid():
            product_selected = form.cleaned_data['product_selected']
            quantity = form.cleaned_data['quantity']
            name = product_selected.product_name
            price = product_selected.product_price
            total = price * quantity
            p = Product.objects.get(product_id=product_selected.product_id)
            p.product_stock -= quantity
            lines = OrderLine.objects.filter(order_id_id=id)
            order_value_dic = OrderLine.objects.filter(order_id_id=id).aggregate(Sum('total'))
            try:
                order_net_value = float(order_value_dic['total__sum'])
                order_gross_value = order_net_value * (1 + tax)
            except TypeError:
                order_net_value = 0.0
                order_gross_value = 0.0
            if p.product_stock >= 0:
                p.save()
                OrderLine.objects.create(quantity=quantity, total=total, order_id_id=id,
                                         product_selected=product_selected, product_selected_name=name)
                return render(request, 'order/addorderlines.html',
                              {'order': order, 'form': form, 'lines': lines, 'order_net_value': order_net_value,
                               "order_gross_value": order_gross_value})
            else:
                text = ('Quantity entered is wrong: enter a positive number. It is possible that there is not enough product in stock.')
                return render(request, 'order/addorderlines.html',
                              {'order': order, 'form': form, 'lines': lines, 'order_net_value': order_net_value,
                               "order_gross_value": order_gross_value, 'text': text})
        else:
            text = (
                'Quantity entered is wrong: enter a positive number. It is possible that there is not enough product in stock.')
            return render(request, 'order/addorderlines.html',
                          {'order': order, 'form': form, 'text': text})


class OrderLineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OrderLine
    permission_required = ('delete_orderline',)
    fields = ['order_id_id', 'selected_product_id', 'selected_product_name', 'quantity', 'total']
    template_name = 'order/delete_orderline.html'
    success_url = '/order/'

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> HOME


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        text_1 = TextBox.objects.get(id=1)
        text_2 = TextBox.objects.get(id=2)
        current_events = Event.objects.filter(end_date__gte=date.today())
        latest_customer = Customer.objects.last()
        latest_order = Order.objects.last()
        return render(request, 'home.html', {'text_1': text_1, 'text_2': text_2, 'current_events': current_events,
                                             'latest_customer': latest_customer, 'latest_order': latest_order})

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDF


class PDF_render_view(View):

    def get(self, request, id):
        order = Order.objects.get(id=id)
        tax = order.get_tax_display()
        lines = OrderLine.objects.filter(order_id_id=id)
        order_value_dic = OrderLine.objects.filter(order_id_id=id).aggregate(Sum('total'))
        try:
            order_net_value = float(order_value_dic['total__sum'])
            order_gross_value = order_net_value * (1 + tax)
        except TypeError:
            order_net_value = 0.0
            order_gross_value = 0.0
        today = date.today()
        params = {
            'today': today,
            'order_gross_value': order_gross_value,
            'order_net_value': order_net_value,
            'order': order,
            'lines': lines,
            'request': request
        }
        return Render.render('pdf.html', params)
