import pytest
from inventory.models import Product, Dealer, Inventory, Order, OrderItem

@pytest.mark.django_db
def test_order_stock_validation():
    product = Product.objects.create(product_name='Brake Pad', selling_price=500, purchase_price=400, stock=5, tax_rate=18.0)
    inventory = Inventory.objects.create(product=product, quantity=5)
    dealer = Dealer.objects.create(name='Test Dealer', phone_number='1234567890')
    order = Order.objects.create(dealer=dealer, status='draft')
    OrderItem.objects.create(order=order, product=product, quantity=10, unit_price=500)
    # Try to confirm order
    assert order.status == 'draft'
    # Simulate confirm logic
    insufficient = []
    for item in order.items.all():
        inv = Inventory.objects.get(product=item.product)
        if item.quantity > inv.quantity:
            insufficient.append({'product': item.product.product_name, 'available': inv.quantity, 'requested': item.quantity})
    assert insufficient[0]['product'] == 'Brake Pad'
    assert insufficient[0]['available'] == 5
    assert insufficient[0]['requested'] == 10

@pytest.mark.django_db
def test_order_status_flow():
    product = Product.objects.create(product_name='Brake Pad', selling_price=500, purchase_price=400, stock=100, tax_rate=18.0)
    inventory = Inventory.objects.create(product=product, quantity=100)
    dealer = Dealer.objects.create(name='Test Dealer', phone_number='1234567890')
    order = Order.objects.create(dealer=dealer, status='draft')
    item = OrderItem.objects.create(order=order, product=product, quantity=10, unit_price=500)
    # Confirm order
    inventory.quantity -= item.quantity
    inventory.save()
    order.status = 'confirmed'
    order.save()
    assert order.status == 'confirmed'
    # Deliver order
    order.status = 'delivered'
    order.save()
    assert order.status == 'delivered'
