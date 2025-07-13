#!/bin/bash
echo "Installing Product Review System Dependencies..."
echo

pip install Django==4.2.7
if [ $? -ne 0 ]; then
    echo "Failed to install Django"
    exit 1
fi

pip install djangorestframework==3.14.0
if [ $? -ne 0 ]; then
    echo "Failed to install Django REST Framework"
    exit 1
fi

pip install django-filter==23.3
if [ $? -ne 0 ]; then
    echo "Failed to install django-filter"
    exit 1
fi

pip install django-cors-headers==4.3.1
if [ $? -ne 0 ]; then
    echo "Failed to install django-cors-headers"
    exit 1
fi

echo
echo "All dependencies installed successfully!"
echo "Now run: python setup.py"
