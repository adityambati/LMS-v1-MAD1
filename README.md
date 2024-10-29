# Library Management System - V1 (LMS-v1-MAD1)
The project, Library Management System Version 1, made for the course Modern Application Development 1, which is part of the IIT-Madras BS Degree in Data Science

![Library Management System Banner](link-to-your-banner-image)

A foundational library management system for managing e-books, sections, and user activities in an organized and efficient way.

## Features

### Admin Features
- **Manage Sections**: Create, update, or delete library sections.
- **Manage E-Books**: Add, edit, or remove e-books from different sections.
- **User Management**: Oversee user information and manage access.

### User Features
- **Browse and Request E-Books**: Users can view available sections and request e-books.
- **Profile Management**: Users can update their profile information and preferences.
- **Feedback Submission**: Users can submit feedback on e-books they’ve read.

## Installation

Follow these steps to set up the project on your local machine:

```bash
# Clone the repository
git clone https://github.com/adityambati/LMS-v1-MAD1.git

# Navigate to the project directory
cd LMS-v1-MAD1

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run
```
## Usage

### Admin Login
- **Credentials**: Use the admin credentials created during setup to access the librarian dashboard.

### User Interaction
1. **Login as a User** – Access e-books and request functionality.
2. **Admin Dashboard** – Access to manage sections, e-books, and view user activity.

## Screenshots

### Login Page
![Login](link-to-login-screenshot)

### Admin Dashboard
![Dashboard](link-to-dashboard-screenshot)

### Book Management Interface
![Manage Books](link-to-book-management-screenshot)

## Technologies Used
- **Flask**: Backend framework for creating APIs and handling application logic.
- **SQLite**: Database for storing e-book and user information.
- **Jinja2**: Template engine for rendering HTML pages.
- **Bootstrap**: CSS framework for styling.

## Project Structure
```plaintext
├── app.py             # Main application file
├── templates/         # HTML templates for pages
├── static/            # Static files (CSS, JS, images)
├── models.py          # Database models
├── routes.py          # Application routes
└── README.md          # Project documentation
