import pytest
from django.test import Client
from django.contrib.auth.models import User
from Clients.models import Order, OrderLine, Product, Category

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def user():
    user = User.objects.create(username='Roman', email='slaw@wp.pl')
    user.set_password('123456')
    return user

@pytest.fixture
def product():
    Product.objects.create(title='1')
    Topic.objects.create(title='2')
    Topic.objects.create(title='3')
    return Product.objects.all()

@pytest.fixture
def customer():
    Customer.objects.create(title='1')
    Customer.objects.create(title='2')
    Customer.objects.create(title='3')
    return Product.objects.all()


@pytest.fixture
def order():
    Order.objects.create()
    return Order.objects.all()

@pytest.fixture
def order_line():
    Order.objects.create()
    return Order.objects.all()