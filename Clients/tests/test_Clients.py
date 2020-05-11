import pytest
from django.contrib.auth.models import User
from django.urls import reverse


def test_access_to_home(client):
    response = client.get('/home')
    assert response.status_code == 301


def test_access_to_wrong_address_failed(client):
    response = client.get('/hemo/')
    assert response.status_code == 302


def test_access_to_customers_list(client):
    response = client.get('/customers_list')
    assert response.status_code == 301


def test_access_to_add_customer(client):
    response = client.get('/add_customer/')
    assert response.status_code == 302


def test_access_to_edit_customer(client):
    response = client.get('/edit_customer/2')
    assert response.status_code == 302


def test_access_to_adress_failed(client):
    response = client.get('/admin')
    assert response.status_code == 200


def test_access_to_delete_customer(client):
    response = client.get('/delete_customer/3')
    assert response.status_code == 302


def test_access_to_calendar(client):
    response = client.get('/calendar/events')
    assert response.status_code == 301


def test_access_to_admin_failed(client):
    response = client.get('/admin')
    assert response.status_code == 200


def test_access_to_products_list(client):
    response = client.get('/products_list')
    assert response.status_code == 301


def test_access_to_edit_product_failed(client):
    response = client.get('/edit_product/1000')
    assert response.status_code == 200


def test_access_to_edit_product(client):
    response = client.get('/edit_product/14')
    assert response.status_code == 302


def test_access_to_add_product(client):
    response = client.get('/add_product/')
    assert response.status_code == 302


def test_access_to_delete_product_failed(client):
    response = client.get('/delete_product/14/')
    assert response.status_code == 302


def test_access_to_delete_product_failed_wrong_product(client):
    response = client.get('/delete_product/1000/')
    assert response.status_code == 302


def test_access_orders(client):
    response = client.get('/orders')
    assert response.status_code == 301


def test_access_to_add_order(client):
    response = client.get('/add_order')
    assert response.status_code == 301


def test_access_edit_order(client):
    response = client.get('/edit_order/6')
    assert response.status_code == 302


def test_access_edit_order_failed(client):
    response = client.get('/edit_order/1')
    assert response.status_code == 200


def test_access_order(client):
    response = client.get('/order/6')
    assert response.status_code == 301


def test_access_order_failed(client):
    response = client.get('/order/2')
    assert response.status_code == 200


def test_access_to_delete_line(client):
    response = client.get('/delete_line/62')
    assert response.status_code == 302


def test_access_to_delete_line_failed(client):
    response = client.get('/delete_line/1')
    assert response.status_code == 200


def test_access_to_map(client):
    response = client.get('/map/')
    assert response.status_code == 200


def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() > 0


@pytest.mark.django_db
def test_user_create_failed():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_user_detail_failed(client, django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
    )
    url = reverse('admin/auth/user/1/change/', kwargs={'pk': user.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'someone' in response.content


