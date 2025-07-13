@echo off
echo Installing Product Review System Dependencies...
echo.

pip install Django==4.2.7
if %errorlevel% neq 0 (
    echo Failed to install Django
    pause
    exit /b 1
)

pip install djangorestframework==3.14.0
if %errorlevel% neq 0 (
    echo Failed to install Django REST Framework
    pause
    exit /b 1
)

pip install django-filter==23.3
if %errorlevel% neq 0 (
    echo Failed to install django-filter
    pause
    exit /b 1
)

pip install django-cors-headers==4.3.1
if %errorlevel% neq 0 (
    echo Failed to install django-cors-headers
    pause
    exit /b 1
)

echo.
echo All dependencies installed successfully!
echo Now run: python setup.py
pause
