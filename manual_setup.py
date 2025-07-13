#!/usr/bin/env python
"""
Manual setup script - step by step setup
Run this if the automatic setup fails
"""

import os
import sys

def main():
    print("Manual Setup for Product Review System")
    print("=" * 40)
    
    if not os.path.exists('manage.py'):
        print("Error: Please run this from the project root directory (where manage.py is located)")
        return
    
    print("\nStep 1: Install dependencies manually")
    print("Run these commands one by one:")
    print("pip install Django==4.2.7")
    print("pip install djangorestframework==3.14.0")
    print("pip install django-filter==23.3")
    print("pip install django-cors-headers==4.3.1")
    
    input("\nPress Enter after installing all dependencies...")
    
    print("\nStep 2: Create migrations")
    print("Run: python manage.py makemigrations reviews")
    input("Press Enter after running the command...")
    
    print("\nStep 3: Apply migrations")
    print("Run: python manage.py migrate")
    input("Press Enter after running the command...")
    
    print("\nStep 4: Create superuser")
    print("Run: python manage.py createsuperuser")
    print("Create a superuser with username 'admin' and password 'admin123'")
    input("Press Enter after creating the superuser...")
    
    print("\nStep 5: Start the server")
    print("Run: python manage.py runserver")
    print("\nYour API will be available at: http://localhost:8000/")
    print("Admin panel at: http://localhost:8000/admin/")
    
    print("\nSetup completed! You can now test the API endpoints.")

if __name__ == '__main__':
    main()
