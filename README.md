# 🚀 Job Platform - Week 1 Project

A full-stack job platform built by **Abdur-Rehman**.

The application scrapes remote jobs, stores them in PostgreSQL, exposes them through a FastAPI backend, and displays them in a modern Next.js frontend.

---

## 📸 Preview

### Home Page
- Browse remote jobs
- Responsive job cards
- Company information
- Categories & Tags

### Job Details
- Complete job description
- Salary
- Job Type
- Category
- Company
- Location
- Apply Link

---

# 🏗 Architecture

```text
                Remotive API
                      │
                      ▼
              Python Scraper
                      │
                      ▼
            StandardJob Schema
                      │
                      ▼
              PostgreSQL Database
                      │
                      ▼
             FastAPI REST API
                      │
                      ▼
              Next.js Frontend
```

---

# ✨ Features

## Backend

- Scrape jobs from Remotive API
- Standardized Job Schema
- FastAPI REST API
- SQLAlchemy ORM
- PostgreSQL Database
- Clean Service Layer Architecture
- Pydantic Validation
- Repository Structure
- HTML Description Cleaning
- Error Handling
- Logging

---

## Frontend

- Next.js App Router
- Responsive UI
- Job Listing Page
- Job Details Page
- API Integration
- Loading States
- Modern Dark Theme

---

# 📂 Project Structure

## Backend

```
app
│
├── config
├── core
├── database
├── models
├── routes
├── schemas
├── scrapper
│   ├── remotive
│   ├── schemas.py
│   └── utils.py
├── services
└── main.py
```

## Frontend

```
app
│
├── job
├── components
├── services
└── page.tsx
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- BeautifulSoup
- Requests

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Axios

---

# 🔄 Data Flow

```text
Remotive API

↓

Python Requests

↓

Parser

↓

StandardJob

↓

JobService

↓

SQLAlchemy Model

↓

PostgreSQL

↓

FastAPI

↓

Next.js

↓

User
```

---

# API Endpoints

## 1. Scrape Jobs

```http
POST /api/job/scrape
```

Fetches the latest jobs from the Remotive API, transforms them into the `StandardJob` format, and stores them in the PostgreSQL database.

### Workflow

```
Remotive API
      │
      ▼
Fetch Jobs
      │
      ▼
Parse & Standardize
      │
      ▼
Save to PostgreSQL
```

Example Response

```json
{
    "message": "Successfully scraped and saved 28 jobs."
}
```

---

## 2. Get All Jobs

```http
GET /api/job/all
```

Returns all stored jobs.

---

## 3. Get Job Details

```http
GET /api/job/{id}
```

Returns the complete details of a selected job.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone <repository-url>
```

---

## Backend

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file.

```env
DATABASE_URL=your_database_url
```

### Run

```bash
uvicorn app.main:app --reload
```

---

## Frontend

Install dependencies

```bash
npm install
```

Run

```bash
npm run dev
```

---

# 🎯 What I Learned

- FastAPI fundamentals
- SQLAlchemy ORM
- PostgreSQL integration
- API design
- Web Scraping
- BeautifulSoup
- Clean Architecture
- Service Layer Pattern
- Data Standardization
- Full-stack communication
- Next.js App Router
- TypeScript

---

# 🔮 Future Improvements

- Multiple job sources
- Generic scraper framework
- Duplicate detection
- Background scheduler
- Docker
- Authentication
- Saved Jobs
- Search & Filters
- Pagination
- CI/CD
- Deployment
- Job Alerts

---

# 👨‍💻 Author

**Abdur Rehman**


GitHub: https://github.com/abdurwebdev

---

⭐ If you found this project helpful, consider giving it a star!