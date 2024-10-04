# Expense Tracker

A Django web application for tracking expenses, integrated with Azure Active Directory (Azure AD) for user authentication.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)
- [Usage](#usage)

## Features

- User authentication via Azure Active Directory
- Expense tracking
- User-friendly interface
- Group-based access control

## Requirements

- Python 3.11 or higher
- Django 5.1.1 or higher
- `django-auth-adfs` package
- Azure Active Directory account

## Setup Instructions
1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to clone the repository using the `cd` command.
   - Run the command:
     git clone https://github.com/Austin-ik/expense_tracker.git
   - Change into the cloned directory:
     cd expense_tracker
     

2. **Create a Virtual Environment:**
   - Ensure you have Python installed on your machine.
   - Run the following command to create a virtual environment:
   - 
     python -m venv venv
     
   - Activate the virtual environment:
     - **On Windows:**
       venv\Scripts\activate
     - **On macOS/Linux:**
       source venv/bin/activate
     

3. **Install the Required Packages:**
   - Ensure the virtual environment is activated (you should see `(venv)` in your prompt).
   - Install the necessary packages by running:
     pip install -r requirements.txt

4. **Configure Azure AD:**
   - Log in to the Azure portal and navigate to the **Azure Active Directory** section.
   - Register a new application:
     - Go to "App registrations" and click on "New registration."
     - Provide a name for your application and set the redirect URI to `http://localhost:8000/oauth2/callback`.
     - Click "Register" to create the application.
   - Obtain the following values:
     - **Client ID**: This is found on the application overview page.
     - **Client Secret**: Go to "Certificates & secrets," then create a new client secret. Make sure to copy the value immediately, as it will not be shown again.
     - **Tenant ID**: This can be found on the Azure Active Directory overview page.

5. **Set up your environment:**
   - Create a `.env` file in the root of your project directory. 
   - Add the following environment variables to the `.env` file with the values obtained from Azure AD:
     - `AAD_CLIENT_ID` - Your application's Client ID.
     - `AAD_CLIENT_SECRET` - Your application's Client Secret.
     - `AAD_TENANT_ID` - Your Azure AD Tenant ID.

6. **Run Database Migrations:**
   - Migrate your database to set up the necessary tables by running:
     python manage.py migrate

7. **Start the Development Server:**
   - Launch the Django development server to begin using the application with the following command:
     python manage.py runserver

## Configuration

- Ensure that the Azure AD configuration is properly set up in your `settings.py` file using the environment variables specified earlier. This includes mapping the necessary claims from Azure AD to your application's user model.

## Usage

- After starting the server, navigate to `http://localhost:8000/welcome` to access the application.
- Click the login link to initiate the Azure AD authentication process. Once authenticated, you will be redirected back to the application.
