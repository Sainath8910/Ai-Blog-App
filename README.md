# 🤖 AI Blog App

A full-stack web application that leverages artificial intelligence to generate, manage, and publish blog content. This application combines Python backend processing with a responsive HTML/CSS frontend to provide an intuitive platform for AI-powered content creation.

---

## ✨ Features

- **AI-Powered Blog Generation** - Automatically generate blog posts using advanced AI models
- **User Authentication** - Secure user registration, login, and authentication system
- **Blog Management** - Create, edit, view, and manage blog posts with ease
- **User Dashboard** - Personalized dashboard displaying user statistics and recent blogs
- **User Profiles** - Create and customize user profiles with bio and preferences
- **Settings Management** - Configure application settings and preferences
- **Export Functionality** - Export blog content in multiple formats
- **Responsive Design** - Mobile-friendly interface for seamless user experience

---

## 🏗️ Project Structure

```
Ai-Blog-App/
├── AI_Blog_Generator/      # AI content generation module
├── ai_pipeline/            # AI pipeline orchestration
├── authentication/         # User authentication system
├── blogs/                  # Blog management module
├── core/                   # Core application logic
├── dashboard/              # User dashboard interface
├── export_app/             # Export functionality
├── profile_app/            # User profile management
├── settings_app/           # Application settings
├── static/                 # Static assets (CSS, JS, images)
├── templates/              # HTML templates
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── build.sh                # Build script
```

---

## 🛠️ Technology Stack

### Backend
- **Python** (44.7%) - Core backend development
- **Django** - Web framework
- **AI/ML Libraries** - For content generation and processing

### Frontend
- **HTML** (52.3%) - Markup and structure
- **CSS** - Styling and responsive design
- **JavaScript** (3%) - Interactive frontend features

### Database
- Relational database for storing users, blogs, and settings

---

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sainath8910/Ai-Blog-App.git
cd Ai-Blog-App
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

---

## 📦 Dependencies

Key packages included in `requirements.txt`:
- Django - Web framework
- Additional AI/ML libraries for blog generation
- Database drivers
- Utility libraries

For a complete list of dependencies, refer to `requirements.txt`

---

## 🎯 Usage

1. **Sign Up** - Create a new user account via the authentication system
2. **Log In** - Access your account with credentials
3. **Generate Blog** - Use the AI Blog Generator to create new content
4. **Manage Blogs** - View, edit, and manage your blog posts
5. **View Dashboard** - Monitor your blog statistics and activity
6. **Customize Profile** - Update your user profile and preferences
7. **Export Content** - Export your blogs in desired formats

---

## 🏗️ Building for Production

Use the provided build script to prepare the application for production:

```bash
bash build.sh
```

---

## 📁 Key Modules

| Module | Purpose |
|--------|---------|
| `authentication/` | Handles user registration, login, and session management |
| `AI_Blog_Generator/` | Generates blog content using AI models |
| `blogs/` | Manages blog CRUD operations and storage |
| `dashboard/` | Displays user statistics and blog overview |
| `profile_app/` | User profile management and customization |
| `export_app/` | Handles blog export in multiple formats |
| `settings_app/` | Application configuration and user preferences |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature requests.

---

## 📄 License

This project is currently unlicensed. Please contact the repository owner for licensing information.

---

## 👤 Author

**Sainath8910** - [GitHub Profile](https://github.com/Sainath8910)

---

## 📞 Support

For support, issues, or questions, please open an issue on the [GitHub repository](https://github.com/Sainath8910/Ai-Blog-App/issues).

---

## 🔮 Future Enhancements

- Multi-language support for blog generation
- Advanced analytics and insights
- Social sharing integration
- Collaborative blog writing features
- SEO optimization tools
- Email notification system

---

**Happy blogging with AI! 🚀**
