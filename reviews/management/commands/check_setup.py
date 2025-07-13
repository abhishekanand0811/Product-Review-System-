from django.core.management.base import BaseCommand
from reviews.models import User, Product, Review

class Command(BaseCommand):
    help = 'Check if the setup is working correctly'

    def handle(self, *args, **options):
        self.stdout.write('Checking Product Review System setup...')
        
        # Check users
        user_count = User.objects.count()
        admin_count = User.objects.filter(role='admin').count()
        regular_count = User.objects.filter(role='regular').count()
        
        self.stdout.write(f'Users: {user_count} total ({admin_count} admin, {regular_count} regular)')
        
        # Check products
        product_count = Product.objects.count()
        self.stdout.write(f'Products: {product_count}')
        
        # Check reviews
        review_count = Review.objects.count()
        self.stdout.write(f'Reviews: {review_count}')
        
        if user_count > 0 and product_count > 0:
            self.stdout.write(self.style.SUCCESS('✓ Setup looks good!'))
            self.stdout.write('You can now run: python manage.py runserver')
        else:
            self.stdout.write(self.style.WARNING('⚠ Run the setup script first: python setup.py'))
