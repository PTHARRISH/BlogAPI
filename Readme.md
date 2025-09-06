# Blog API - Django REST Framework

A comprehensive Blog API built with Django REST Framework that provides JWT authentication, user management, and full CRUD operations for blog posts with pagination support and Swagger documentation.

![Python](https://img.shields.io/badge/Python-80.9%25-blue)


## 🚀 Features

- **User Management**
  - User Registration with validation
  - Profile Updates for authenticated users
  - JWT Token Authentication
  - Session-based authentication for Swagger UI

- **Blog Management**
  - Create Blog Posts (Authenticated users only)
  - Read Blog Posts (Public access with pagination)
  - Update Blog Posts (Author only)
  - Delete Blog Posts (Author only)
  - Paginated responses (3 items per page)

- **API Documentation**
  - Interactive Swagger UI documentation
  - ReDoc documentation
  - JWT token integration in Swagger

- **Security & Performance**
  - Permission-based access control
  - Author verification for blog modifications
  - JWT token authentication with refresh
  - Optimized database queries

## 📋 Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt
- drf-yasg (for Swagger documentation)

## 🛠️ Installation

1. **Clone the repository**
   
   git clone https://github.com/PTHARRISH/BlogAPI.git
   cd BlogAPI

2. **Create virtual environment**
   
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate

3. **Install dependencies**
   
   pip install -r requirements.txt

4. **Configure environment variables**
   
   cp .env.example .env
   
   Edit .env file with your configuration:
   - SECRET_KEY=your-secret-key-here

5. **Run migrations**
   
   python manage.py makemigrations
   python manage.py migrate

6. **Create superuser** (Optional)
   
   python manage.py createsuperuser

7. **Start development server**
   
   python manage.py runserver

8. **Access the API**
   - API Base URL: http://localhost:8000/api/
   - Swagger Documentation: http://localhost:8000/swagger/
   - ReDoc Documentation: http://localhost:8000/redoc/

## 📡 API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/token/` | Obtain JWT token pair | No |
| POST | `/api/token/refresh/` | Refresh JWT access token | No |
| POST | `/api/register_users/` | Register new user | No |
| PUT | `/api/update_user_profile/` | Update user profile | Yes |

### Blog Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/blog_list/` | Get paginated blog list | No |
| POST | `/api/create_blog/` | Create new blog post | Yes |
| POST | `/api/update_blog/<int:pk>/` | Update specific blog | Yes (Author only) |
| POST | `/api/delete_blog/<int:pk>/` | Delete specific blog | Yes (Author only) |




## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Harrish P T**
- GitHub: [@PTHARRISH](https://github.com/PTHARRISH)
- Email: harrish@example.com

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Thank You for Exploring BlogAPI!

Thank you for taking the time to explore this Blog API project! This comprehensive Django REST Framework application demonstrates modern API development practices with JWT authentication, interactive documentation, and clean architecture.

### 🌟 What Makes This Project Special:

- **Production-Ready:** Built with industry best practices
- **Well-Documented:** Complete API documentation with Swagger UI
- **Secure:** JWT authentication with proper authorization
- **Developer-Friendly:** Interactive API testing with Swagger
- **Scalable:** Clean, maintainable codebase

### 🚀 Ready to Get Started?

1. **Star this repository** if you find it helpful! ⭐
2. **Fork it** to create your own version
3. **Contribute** by submitting pull requests
4. **Share** with fellow developers

### 💬 Need Help?

- Check out the [Issues](https://github.com/PTHARRISH/BlogAPI/issues) page
- Create a new issue for bugs or feature requests
- Connect with me on GitHub: [@PTHARRISH](https://github.com/PTHARRISH)

### 🎯 Happy Coding!

Whether you're learning Django REST Framework, building your own blog API, or just exploring modern web development, I hope this project serves as a valuable resource. Keep coding, keep learning, and keep building amazing things!

**Remember: The best way to learn is by doing. So clone this repository, experiment with the code, and make it your own!**

---

*Built with ❤️ by [Harrish P T](https://github.com/PTHARRISH)*
