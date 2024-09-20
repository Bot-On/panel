# Django Project "Panel" - Installation Guide

This project is built using **Django**, and the following steps will guide you through setting up the project locally using a virtual environment (venv) and installing the dependencies listed in the `requirements.txt` file.

## Prerequisites

Make sure you have the following installed on your machine:

- **Python** (Ensure you have a working version of Python)
- **pip** (Python package manager)
- **virtualenv** (Optional, but recommended for isolating project dependencies)

## Development Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/Bot-On/panel.git
cd panel
```

### 2. Create a virtual environment

Use **virtualenv** to create a virtual environment and isolate the project dependencies to avoid conflicts with other projects.

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies

Once the virtual environment is activated, install the required dependencies listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure the staging database

In the **Django** configuration file (`settings.py`), configure the connection to the **staging** environment database.

#### Example configuration for a PostgreSQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'staging_db_name',
        'USER': 'staging_db_user',
        'PASSWORD': 'staging_db_password',
        'HOST': 'staging_db_host',
        'PORT': 'staging_db_port',
    }
}
```
