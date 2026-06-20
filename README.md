# BGMI FastAPI Backend

A FastAPI-based backend application for BGMI-style player management, authentication, match tracking, and leaderboard generation.

## Features

- User Registration
- User Login with JWT Authentication
- MongoDB Database Integration
- Match Recording API
- Leaderboard Generation
- WebSocket Support
- Interactive Swagger API Documentation
- Environment Variable Configuration
- Modular Project Structure

## Tech Stack

- Python 3.11+
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- JWT (python-jose)
- Passlib (Password Hashing)
- Uvicorn

## Project Structure

```text
bgmi_fastapi_pro/
│
├── main.py
├── database.py
├── auth_utils.py
├── schemas.py
├── requirements.txt
├── .env.example
│
├── routers/
│   ├── auth.py
│   └── player.py
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/bgmi_fastapi_pro.git
cd bgmi_fastapi_pro
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
MONGO_URL=mongodb://localhost:27017
JWT_SECRET=your_secret_key
```

## Run Server

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | `/api/auth/register` | Register User |
| POST | `/api/auth/login` | Login User |

### Player

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | `/api/player/match` | Add Match Record |
| GET | `/api/player/leaderboard` | Get Top Players |

### Root

| Method | Endpoint |
|----------|----------|
| GET | `/` |

## Sample Register Request

```json
{
  "username": "akarshit",
  "password": "123456"
}
```

## Sample Login Request

```json
{
  "username": "akarshit",
  "password": "123456"
}
```

## Future Enhancements

- Role-Based Authentication
- Refresh Tokens
- Tournament Management
- Team Management
- Clan System
- Match Analytics
- Docker Deployment
- MongoDB Atlas Integration
- CI/CD Pipeline

## Author

**Akarshit Bansal**

Python Developer | FastAPI Developer | Backend Engineer

## License

This project is licensed under the MIT License.
