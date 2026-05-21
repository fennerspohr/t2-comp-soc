# BDEdica - Socioeducational Management System

BDEdica is a full-stack web application developed to help non-governmental organizations (NGOs) efficiently manage and track socioeducational measures (MSEs). The system simplifies complex workflows by allowing users to register, list, edit, and filter sensitive data through a highly secure and intuitive interface.

---

## Focus on User Experience (UX)
The core frontend of this project was designed from the ground up with a strong emphasis on **User Experience**. Managing administrative data can be overwhelming, so we focused on creating:
* **Clean & Responsive Layouts:** Seamless navigation across different screen sizes.
* **Intuitive Workflows:** Advanced filtering and data visualization made simple for the end-user.
* **Component-Driven UI:** Built using high-quality UI components to ensure visual consistency and accessibility.

---

## Tech Stack

### Frontend
* **Vue.js** (Options/Composition API)
* **Tailwind CSS** (Utility-first styling)
* **DaisyUI** (Tailwind CSS component library)
* **Axios** (HTTP client for API communication)

### Backend
* **Python**
* **Django REST Framework (DRF)** (Scalable RESTful API architecture)
* **MySQL** (Relational database management)

---

## Key Features
* **Authentication & Authorization:** Secure login system for organization members.
* **Socioeducational Measures Management:** Full CRUD (Create, Read, Update, Delete) capabilities for MSEs.
* **Advanced Data Filtering:** Dynamic search and filtering system to locate specific records quickly.
* **API Integration:** Seamless, real-time data sync between the Vue.js frontend and Django backend.

---

## Getting Started

### Prerequisites
Make sure you have the following installed:
* [Node.js](https://nodejs.org/) (for the frontend)
* [Python 3.x](https://www.python.org/) (for the backend)
* [MySQL](https://www.mysql.com/)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/fennerspohr/t2-comp-soc.git](https://github.com/fennerspohr/t2-comp-soc.git)
   cd t2-comp-soc

2. **Backend Setup (Django):**
   ```bash
   # Navigate to backend folder (adjust directory name if needed)
    cd backend
    # Install dependencies
    pip install -r requirements.txt
    # Run database migrations
    python manage.py migrate
    # Start the server
    python manage.py runserver 

3. **Frontend Setup (Vue.js):**
   ```bash
   # Navigate to frontend folder (adjust directory name if needed)
    cd ../frontend
    # Install dependencies
    npm install
    # Start the development server
    npm run dev

### License
This project was developed for academic and social impact purposes.
