# MiniBlog Project

## Overview

MiniBlog is a robust, Flask-based microblogging platform that allows users to share short posts, follow other users, and engage with a community of writers and thinkers. Built with modern web development practices, MiniBlog showcases the power of Python and Flask in creating responsive, user-friendly web applications.

## Features

### User Authentication
- Secure login and registration system

### User Profiles
- Customizable user profiles with avatars and "about me" sections

### Post Creation
- Users can create and share short posts

### Follow System
- Users can follow/unfollow other users

### Timeline
- Personalized timeline showing posts from followed users

### Pagination
- Efficient loading of posts through pagination

### Password Reset
- Secure password reset functionality via email

### Exploration
- Discover new content and users through the explore page

### Multilingual Support
The miniblog app now supports multiple languages, allowing you to reach a broader audience. This feature is powered by PyBabel for message translation and localization.

### Custom CLI Commands
To streamline language management, custom CLI commands have been added to the Flask command. These commands help with extracting, compiling, and updating translation files.

**Commands:**
- Initialize Translations: `flask translate init <language-code>`
- Update Translations: `flask translate update`
- Compile Translations: `flask translate compile`

These commands ensure seamless translation management and are essential for deploying the miniblog app with multilingual support.

## Technical Stack

- Backend: Flask (Python)
- Database: SQLAlchemy ORM
- Authentication: Flask-Login
- Frontend: Jinja2 templates

**Additional Libraries:**
- Werkzeug for password hashing
- PyJWT for token-based password reset
- Flask-WTF for form handling

## Project Structure

- `models.py`: Defines the database models (User and Post)
- `routes.py`: Contains all the route handlers for the application
- `forms.py`: Defines forms used in the application
- `email.py`: Handles email functionality for password reset

## Setup and Installation

(Include steps for setting up the project, such as creating a virtual environment, installing dependencies, setting up the database, etc.)

## Running the Application

(Provide instructions on how to run the application locally)

## Future Enhancements

- Implement post likes and comments
- Add user search functionality
- Integrate with external APIs for rich content sharing
- Implement real-time notifications