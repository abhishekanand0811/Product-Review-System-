#!/usr/bin/env python
"""
made this file to fix migration issues by resetting the database
run this script to clean up and recreate everything
"""

import os
import sys
import subprocess

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print("Error:", result.stderr)
    return result.returncode == 0

def main():
    print("Fixing migration issues...")
    
    if not os.path.exists('manage.py'):
        print("Error: manage.py not found. Please run this script from the project root directory.")
        return
    
    # Step 1: Remove existing database
    print("\n1. Removing existing database...")
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
        print("Database removed.")
    else:
        print("No existing database found.")
    
    # Step 2: Remove migration files except __init__.py
    print("\n2. Cleaning migration files...")
    migrations_dir = 'reviews/migrations'
    if os.path.exists(migrations_dir):
        for file in os.listdir(migrations_dir):
            if file.endswith('.py') and file != '__init__.py':
                file_path = os.path.join(migrations_dir, file)
                os.remove(file_path)
                print(f"Removed {file_path}")
    
    # Step 3: Create new migrations
    print("\n3. Creating fresh migrations...")
    if not run_command("python manage.py makemigrations reviews"):
        print("Failed to create migrations.")
        return
    
    # Step 4: Apply migrations
    print("\n4. Applying migrations...")
    if not run_command("python manage.py migrate"):
        print("Failed to apply migrations.")
        return
    
    # Step 5: Create superuser
    print("\n5. Creating superuser...")
    run_command('python manage.py shell -c "from reviews.models import User; User.objects.create_superuser(\'admin\', \'admin@example.com\', \'admin123\', role=\'admin\') if not User.objects.filter(username=\'admin\').exists() else print(\'Superuser already exists\')"')
    
    # Step 6: Create sample data
    print("\n6. Creating sample data...")
    create_sample_data()
    
    print("\n✅ Migration issues fixed!")
    print("\nTest accounts created:")
    print("- Superuser: admin / admin123")
    print("- Admin user: admin_user / password123")
    print("- Regular users: user1, user2, user3 / password123")
    print("\nYou can now start the development server with:")
    print("python manage.py runserver")

def create_sample_data():
    
    user_creation_script = '''
from reviews.models import User, Product, Review

# Create admin user
admin_user, created = User.objects.get_or_create(
    username='admin_user',
    defaults={'email': 'admin@test.com', 'role': 'admin'}
)
if created:
    admin_user.set_password('password123')
    admin_user.save()
    print("Admin user created: admin_user")

# Create regular users
regular_users = []
for i in range(1, 4):
    user, created = User.objects.get_or_create(
        username=f'user{i}',
        defaults={'email': f'user{i}@test.com', 'role': 'regular'}
    )
    if created:
        user.set_password('password123')
        user.save()
        print(f"Regular user created: user{i}")
    regular_users.append(user)

# Create sample products
products_data = [
    {
        'name': 'Wireless Bluetooth Headphones',
        'description': 'High-quality wireless headphones with noise cancellation and 30-hour battery life.',
        'price': 199.99
    },
    {
        'name': 'Smart Fitness Tracker',
        'description': 'Advanced fitness tracker with heart rate monitoring, GPS, and sleep tracking.',
        'price': 149.99
    },
    {
        'name': 'Portable Laptop Stand',
        'description': 'Ergonomic aluminum laptop stand that is lightweight and adjustable.',
        'price': 49.99
    }
]

products = []
for product_data in products_data:
    product, created = Product.objects.get_or_create(
        name=product_data['name'],
        defaults={
            'description': product_data['description'],
            'price': product_data['price'],
            'created_by': admin_user
        }
    )
    if created:
        print(f"Product created: {product.name}")
    products.append(product)

# Create sample reviews
if len(products) >= 2 and len(regular_users) >= 2:
    reviews_data = [
        {'product': products[0], 'user': regular_users[0], 'rating': 5, 'comment': 'Excellent sound quality and battery life!'},
        {'product': products[0], 'user': regular_users[1], 'rating': 4, 'comment': 'Great headphones, worth the price.'},
        {'product': products[1], 'user': regular_users[0], 'rating': 4, 'comment': 'Good fitness tracker with accurate monitoring.'},
    ]
    
    for review_data in reviews_data:
        review, created = Review.objects.get_or_create(
            product=review_data['product'],
            user=review_data['user'],
            defaults={
                'rating': review_data['rating'],
                'comment': review_data['comment']
            }
        )
        if created:
            print(f"Review created: {review.user.username} -> {review.product.name}")

print("Sample data creation completed!")
'''
    
    
    with open('temp_data_script.py', 'w') as f:
        f.write(user_creation_script)
    
    run_command('python manage.py shell < temp_data_script.py')
    
    
    if os.path.exists('temp_data_script.py'):
        os.remove('temp_data_script.py')

if __name__ == '__main__':
    main()
