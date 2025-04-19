
![Samir List Banner](https://raw.githubusercontent.com/abdallasamir04/Samir-List/main/Samir%20List/files/todobanner.png.png)

# Samir List : Organize Your Life

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-yellow.svg?style=for-the-badge&logo=python&logoColor=white)

The **Samir List** is a task management web application built with **Flask** and **SQLAlchemy** that allows users to efficiently organize, track, and complete their daily tasks. 

> 🧠 Developed by **Abdalla Samir** at **Assiut National University**, Faculty of Computers and Artificial Intelligence  
> 📚 For the **Software Design and Architecture** course – 3rd Level

---

## 🚀 Features

### 🔧 Task Management
- Add new tasks with custom **titles**, **descriptions**, and **priority**.
- Organize tasks into categories (active, completed).
- Edit or delete tasks at any time.

### ✅ Active Tasks & Completed Tasks
- View tasks marked as **active** or **completed**.
- Easily toggle task status to mark them as completed.
  
### 📱 User Authentication
- Users can **register** and **login** to securely access their tasks.
- Each user has their own task list, keeping everything private.

### 🌈 Intuitive User Interface
- Clean and simple interface for creating, editing, and deleting tasks.
- Responsive design for mobile and desktop devices.

### 🖼️ Profile Management
- Users can upload a **profile picture** and update their **personal information**.

### 💾 Data Persistence
- Tasks and user data are **saved to a database** with SQLAlchemy for reliability.

---

## 📦 Getting Started

### 📋 Requirements
- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- Flask-WTF (For forms)
- Flask-Login (For authentication)
  
### ⚙️ Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/samir_list.git
   ```

2. **Navigate to the project folder:**
   ```bash
   cd samir_list
   ```

3. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the app:**
   ```bash
   flask run
   ```
   This will start the server locally. You can access the application by visiting [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 💡 Example Screenshots


### index (After Login)

![index](https://raw.githubusercontent.com/abdallasamir04/Samir-List/main/Samir%20List/files/afterlogin.png)

### Dashboard 
![Dashboard](https://raw.githubusercontent.com/abdallasamir04/Samir-List/main/Samir%20List/files/Dashboared.png)

### edit Page
![edit](https://raw.githubusercontent.com/abdallasamir04/Samir-List/main/Samir%20List/files/edit.png)

---

# 📁 Project Directory Tree

```bash
project_root/
  ├── app.py                # Main entry point of the application
  ├── config.py             # Configuration settings (e.g., secret key, database URI)
  ├── models.py             # SQLAlchemy models for User and Todo
  ├── routes.py             # Routes for login, logout, task management
  ├── templates/            # HTML templates for views
  │   ├── base.html         # Base layout for the site
  │   ├── index.html        # Homepage template
  │   ├── login.html        # Login page template
  │   └── dashboard.html    # Dashboard for managing tasks
  ├── static/               # Static files (CSS, JS, images)
  │   ├── css/              # Stylesheets
  │   │   └── style.css     # Custom styles
  │   ├── js/               # JavaScript files
  │   │   └── your-script.js# Custom JavaScript logic
  │   └── images/           # Images (e.g., logos, icons)
  ├── migrations/           # Database migration files (auto-generated)
  └── todo/                 # Todo-related files
      ├── routes.py         # Todo-specific routes for managing tasks
      └── models.py         # Todo-specific models (for tasks)
```

---

## 📋 Example Use Case

### **Add Task**
To add a task, navigate to the "Add Task" page and provide the **title**, **description**, and **priority** for the task. After the task is added, it will appear in the dashboard under "Active Tasks". You can mark it as completed once done.

### **Toggle Task Completion**
The tasks can be toggled between **active** and **completed** by clicking the respective action button. The status will update accordingly, and the task will move between the two sections on the dashboard.

### **Edit or Delete Task**
You can edit or delete any task. Editing allows you to change the task's details such as title, description, and priority. Deleting removes the task from the system entirely.


---

## 🔗 Dependencies

- **Flask** – Python web framework for building the app.
- **Flask-SQLAlchemy** – SQLAlchemy ORM to interact with the database.
- **Flask-WTF** – Form handling and CSRF protection.
- **Flask-Login** – User session management and authentication.


---

## 🙏 Acknowledgments

    Eng. Mohamed Sayed Osman - Technical guidance.

    
## 📧 Contact

Let's connect! Feel free to reach out or follow me on these platforms:  

[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/abdallasamir04/)  
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/abdallasamir04)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdalla-mahmoud-9264242b6/)  
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:samirovic707@gmail.com)  
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abdallasamir04)  
---
**Abdalla Mahmoud Samir**  
**Faculty of Computers and Artificial Intelligence**  
**Assiut National University**  
**Software Design and Architecture Course - Third Level**  **April 2025**


