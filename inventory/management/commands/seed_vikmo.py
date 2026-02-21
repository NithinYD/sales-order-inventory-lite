from inventory.models import Product, Dealer, Inventory, Order, OrderItem, Category, Warehouse, Supplier

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seed sample data for Vikmo assignment'

    def handle(self, *args, **kwargs):
        # Create sample category
        category, _ = Category.objects.get_or_create(category_name='Brakes')
        # Create sample warehouse
        warehouse, _ = Warehouse.objects.get_or_create(warehouse_name='Main Warehouse')
        # Create sample supplier
        supplier, _ = Supplier.objects.get_or_create(supplier_name='Default Supplier', phone_number='0000000000')
        # Create sample product
        product, _ = Product.objects.get_or_create(
            product_name='Brake Pad',
            selling_price=500,
            purchase_price=400,
            stock=100,
            tax_rate=18.0,
            category=category,
            warehouse=warehouse,
            supplier=supplier
        )
        # Create inventory record
        Inventory.objects.get_or_create(product=product, quantity=100)
        # Create dealer
        dealer, _ = Dealer.objects.get_or_create(
            name='ABC Motors',
            phone_number='1234567890',
            email='abc@example.com'
        )
        # Create draft order
        order = Order.objects.create(dealer=dealer, status='draft')
        OrderItem.objects.create(order=order, product=product, quantity=10, unit_price=500)
        self.stdout.write(self.style.SUCCESS('Sample data seeded successfully.'))
