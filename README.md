# 🚀 Emotion Recognition API

A powerful **Django + DRF backend** for real-time **emotion detection from video streams**.  
Handles **user authentication** and **emotion analysis** with an integrated machine learning model — perfect for adding emotion intelligence to your applications.

<p align="center">
<a href="https://github.com/Anugrxh/Mini-Project-Backend/stargazers">
<img src="https://img.shields.io/github/stars/Anugrxh/Mini-Project-Backend?style=social" alt="GitHub stars">
</a>
<a href="https://github.com/Anugrxh/Mini-Project-Backend/network/members">
<img src="https://img.shields.io/github/forks/Anugrxh/Mini-Project-Backend?style=social" alt="GitHub forks">
</a>
<a href="https://github.com/Anugrxh/Mini-Project-Backend/issues">
<img src="https://img.shields.io/github/issues/Anugrxh/Mini-Project-Backend" alt="GitHub issues">
</a>
<a href="https://github.com/Anugrxh/Mini-Project-Backend/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/Anugrxh/Mini-Project-Backend" alt="License">
</a>
</p>

---

## 🌟 Introduction  
This backend is part of an **Emotion Recognition System** built using Django and Django REST Framework.  
It provides:  
- Secure **JWT-based authentication**  
- Video upload and **real-time emotion analysis**  
- Scalable REST API endpoints for easy integration  

---

## 🛠️ Tech Stack  

**Backend:** Django, Django REST Framework  
**Database:** SQLite  
**Authentication:** JWT (JSON Web Tokens)  
**Machine Learning:** TensorFlow, Keras, OpenCV *(specify exact ML libs used)*  
**Environment:** Python `venv`  
**Media Handling:** Django's built-in file upload handling  

---

## ⚙️ Installation & Setup  

### **Prerequisites**
- Python 3.8+  
- `pip` (Python package installer)  

### **Steps**
```bash
# 1️⃣ Clone the repository
git clone https://github.com/Anugrxh/Mini-Project-Backend.git
cd Mini-Project-Backend

# 2️⃣ Create & activate virtual environment
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run migrations
python manage.py migrate

# 5️⃣ Start the server
python manage.py runserver
```
Your API will be available at: **http://127.0.0.1:8000**  

---

## 🎯 API Endpoints  

**Base URL:** `http://127.0.0.1:8000/api/`  

### **1. User Authentication**  

#### **Signup**
- **POST** `/signup/`  
- Registers a new user.  
- **Body (JSON)**:
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "mobile": "9876543210",
  "password": "StrongPass123"
}
```
- **Response:** JWT token on success.

#### **Login**
- **POST** `/login/`  
- Authenticates user & returns token.  
- **Body (JSON)**:
```json
{
  "email": "john@example.com",
  "password": "StrongPass123"
}
```
- **Response:**
```json
{
  "token": "your_jwt_token"
}
```

---

### **2. Emotion Recognition**  

#### **Upload & Analyze Video**
- **POST** `/emotion-video/`  
- **Headers:**  
  `Authorization: Bearer <your_token>`  
- **Body (multipart/form-data)**:  
  Key: `video`, Value: `.mp4` file  
- **Response:** JSON with detected emotions.

**Example cURL:**
```bash
curl -X POST   http://127.0.0.1:8000/api/emotion-video/   -H 'Authorization: Bearer <your_login_token>'   -F 'video=@/path/to/video.mp4'
```

---

## 🤝 Contributing  
Contributions are welcome!  
- Fork the repo  
- Create a new branch  
- Submit a PR  
See **CONTRIBUTING.md** for details.

---

## 📝 License  
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact  
**Anugrah M**  
📩 Email: anugrahmadha@gmail.com  
🔗 Project Link: [Mini-Project-Backend](https://github.com/Anugrxh/Mini-Project-Backend)  
