#!/bin/bash

# Create backend directory
mkdir backend
cd backend

# Create app directory and main FastAPI file
mkdir app
cd app
touch main.py

# Create API directory with routers and models subdirectories
mkdir api
cd api
mkdir routers models
touch __init__.py routers/fraud.py routers/reports.py routers/auth.py models/fraud.py models/reports.py models/auth.py

# Create services directory
cd ..
mkdir services
cd services
touch __init__.py fraud_service.py report_service.py auth_service.py

# Create database directory with models and connection files
cd ..
mkdir database
cd database
touch __init__.py models.py connection.py

# Create security directory with authentication and security utility files
cd ..
mkdir security
cd security
touch __init__.py auth_utils.py security_utils.py

# Create utils directory with common utility functions
cd ..
mkdir utils
cd utils
touch __init__.py common_utils.py

# Move back to the backend directory
cd ../..