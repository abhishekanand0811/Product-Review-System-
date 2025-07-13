# Product Review System API

A comprehensive RESTful API and web application for a Product Review System built with Django and Django REST Framework. Features role-based access control, product management, and a complete review system with rating aggregation.

## 🌟 Features

### 🔐 **User Authentication & Authorization**
- **Role-based Access Control**: Admin and Regular user roles
- **Session Authentication**: Web interface login/logout
- **User Registration**: Self-service account creation

### 📦 **Product Management**
- **Admin Product Control**: Create, update, delete products
- **Product Catalog**: Browse products with search and filtering
- **Product Details**: Comprehensive product information
- **Price Management**: Decimal precision pricing

### ⭐ **Review System**
- **Rating System**: 1-5 star ratings with visual display
- **Review Comments**: Detailed feedback from users
- **One Review Per User**: Prevents duplicate reviews
- **Rating Aggregation**: Automatic average rating calculation
- **Review Count**: Track total reviews per product

### 🎨 **Frontend Interface**
- **Modern UI**: Bootstrap-based clean interface
- **Search Functionality**: Find products quickly
- **User Dashboard**: Personal review management
- **Pagination**: Efficient data browsing

### 🔧 **API Features**
- **RESTful Design**: Standard HTTP methods and status codes
- **Comprehensive Filtering**: Search, filter, and sort data
- **Data Validation**: Input validation and error handling
- **CORS Support**: Frontend integration ready

## 🚀 Quick Start

### Installation

1. **Clone or download the project**
   ```bash
   cd product-review-api
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Run the automated setup**
   ```bash
   python fix_migrations.py
   ```
   
   This will:
   - Install all dependencies
   - Set up the database
   - Create sample data
   - Set up test accounts

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - **Frontend**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/
   - **API Root**: http://127.0.0.1:8000/api/

## 👥 Test Accounts

After setup, you can use these pre-created accounts:

### Regular Users (Can browse and review products)
- **Username**: `user1`, `user2`, `user3`
- **Password**: `password123`

### Admin Users (Can manage products)
- **Username**: `admin_user`
- **Password**: `password123`

### Superuser (Full system access)
- **Username**: `admin`
- **Password**: `admin123`

## 🚨 Troubleshooting

### Common Issues

1. **Migration Errors**
   ```bash
   python fix_migrations.py
   ```

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission Denied**
   - Ensure you're in the project root directory
   - Check file permissions on Unix systems

4. **Database Issues**
   - Delete `db.sqlite3` and run migrations again
   - Use the fix_migrations.py script

5. **Import Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

## 📝 License

This project is created for educational and demonstration purposes. Feel free to use and modify as needed.

## 🤝 Contributing

This is a technical assignment project. For improvements or suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
---
**Built with ❤️ using Django and Django REST Framework**
