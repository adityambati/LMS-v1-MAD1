# Library Management System - V1 (LMS-v1-MAD1)
The project, Library Management System Version 1, made for the course Modern Application Development 1, which is part of the IIT-Madras BS Degree in Data Science

<img src="/images/banner.png" alt="Banner" width="600">

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
python app.py
```
## Usage

### User Interaction
1. **Login as a User** – Access e-books and request functionality.
2. **Admin Dashboard** – Access to manage sections, e-books, and view user activity.

## Screenshots

### Login Page
<img src="/images/UserLogin.png" alt="User Login" width="600">

### User Dashboard
<img src="/images/UserBooks.png" alt="User Dashboard 1" width="600">
<img src="/images/UserDashAllBooks.png" alt="User Dashboard 2" width="600">

### Admin Dashboard
<img src="/images/AdminDash2.png" alt="Admin Dashboard 1" width="600">

### Book Management Interface
<img src="/images/AdminDash1.png" alt="Admin Dashboard 2" width="600">

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
└── README.md          # Project documentation
```

## Future Scope
- **Advanced Dashboard Features** - Adding caching and batch job capabilities.
- **Enhanced User Notifications** - Automated email reminders and reporting.
- **Improved UI** - A better user interface, as currently its basic.

## LICENSE
This project is licensed under the MIT License. See <a href="https://github.com/adityambati/LMS-v1-MAD1/blob/main/LICENSE">LICENSE<a/> for details.
