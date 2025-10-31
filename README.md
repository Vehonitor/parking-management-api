# Parking Management API

## Overview

The Parking Management API is a FastAPI application designed to manage parking spots, user authentication, and related functionalities. It is configured for deployment on AWS Lambda, allowing for scalable and serverless operation.

## Features

- User authentication (signup and login)
- CRUD operations for parking spots
- Health check endpoint
- Integration with Google Maps and Razorpay for enhanced functionalities

## Project Structure

```
parking-management-api
├── src
│   ├── main.py
│   ├── handler.py
│   ├── api
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── routers
│   │       │   ├── auth.py
│   │       │   ├── parking.py
│   │       │   └── health.py
│   │       ├── schemas
│   │       │   ├── parking.py
│   │       │   └── user.py
│   │       └── dependencies.py
│   ├── core
│   │   ├── config.py
│   │   └── security.py
│   ├── db
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models
│   │       ├── user.py
│   │       └── parking_spot.py
│   ├── services
│   │   ├── parking_service.py
│   │   └── auth_service.py
│   ├── repositories
│   │   ├── user_repo.py
│   │   └── parking_repo.py
│   ├── utils
│   │   └── logger.py
│   └── tests
│       ├── conftest.py
│       ├── test_parking.py
│       └── test_auth.py
├── alembic
│   ├── env.py
│   └── versions
├── serverless.yml
├── requirements.txt
├── Dockerfile
├── Makefile
├── .github
│   └── workflows
│       ├── ci.yml
│       └── deploy.yml
├── .gitignore
├── .env.example
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/parking-management-api.git
   cd parking-management-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
   ```

powershell
.\venv\Scripts\Activate.ps1

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and fill in the required values.

5. **Run the application locally:**
   ```bash
   uvicorn src.main:app --reload
   ```

## Deployment Instructions

1. **Install Serverless Framework:**
   ```bash
   npm install -g serverless
   ```

2. **Deploy to AWS Lambda:**
   ```bash
   serverless deploy
   ```

## API Reference

- **POST /api/v1/auth/signup**: User signup
- **POST /api/v1/auth/login**: User login
- **GET /api/v1/parking**: List parking spots
- **POST /api/v1/parking**: Create a new parking spot
- **GET /api/v1/health**: Health check

## Documentation

- [Architecture](architecture.md)
- [Database Schema](database_schema.md)
- [Deployment Guide](deployment_guide.md)
- [API Reference](api_reference.md)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.



pip install twilio psycopg2-binary python-dotenv