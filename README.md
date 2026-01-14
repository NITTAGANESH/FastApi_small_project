🚀 GN TECH Trac – Product Management System

A full-stack Product Management System built using FastAPI, MySQL, JWT Authentication, Role-Based Authorization, and React.

This project demonstrates real-world backend security, role control, and frontend integration

📌 Features
🔐 Authentication & Authorization

JWT based login using email & password

Role based access control (Admin / User)

Only one admin allowed in system

Token protected APIs

👥 Roles:
  Role	Permissions
  User	View products
  Admin	Add, Edit, Delete products

📦 Product Management:
  Add product
  Edit product
  Delete product
  Search, sort & filter
  Secure API access

🎨 Frontend:
  Modern UI with React
  Login page
  Register page
  Protected routes
  Axios JWT interceptor
  Role based UI

🛠 Tech Stack
Backend:
  FastAPI
  SQLAlchemy
  MySQL
  JWT (python-jose)
  Passlib (bcrypt)
  OAuth2

Frontend:
  React
  Axios
  React Router
  CSS

NOTE:
-> To run frontend cmd: 
          1.npm install
          2.npm start
-> To run backend:
          1.It is Uvicorn server so use command uvicorn main:app --relod
