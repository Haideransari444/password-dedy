# 🟥 Password Dedy

> A peer-to-peer platform to lend and borrow premium digital accounts affordably and securely — built for students.

---

## 📌 Project Overview

**Password Dedy** is a peer-to-peer platform where students can lend and borrow premium digital accounts (e.g., Netflix, Canva, ChatGPT) securely. Users can list accounts, set prices, control visibility, and chat in-app with borrowers. Designed to meet real student needs with affordability, privacy, and flexibility.

---

## 🧠 Infographics

| 🎯 **Target Users**     | 🔒 **Security**             | 💬 **Communication**          | 💸 **Monetization**           |
|-------------------------|------------------------------|-------------------------------|-------------------------------|
| Students looking for affordable premium tools | Visibility control, session auth, moderation | Borrowers chat with lenders directly | Listing fees via PayFast for secure earnings |

---

## 🚀 Key Features

- ✅ **Email-based registration and login**  
- 🔐 **Session authentication with CSRF protection**  
- 📤 **Create, delete, and toggle listing visibility**  
- 💬 **In-app borrower/lender chat**  
- 🔔 **Notifications panel**  
- 🛡️ **Admin moderation tools**  
- 💳 **PayFast integration for listing fees**  

---

## 🛠 Tech Stack

- 🧩 **Backend:** Django + Django REST Framework  
- 🗃️ **Database:** Supabase (PostgreSQL)  
- 🎨 **Frontend:** React (via V0.dev)  
- 🔐 **Auth:** Custom Django user model  
- 🖼️ **Media:** Cloudinary  
- 🌐 **Hosting:** Render  
- 💸 **Payments:** PayFast API  

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/password-dedy.git
cd password-dedy
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📁 Project Structure

- `accounts/` — Auth and registration  
- `listings/` — Listings models, views, endpoints  
- `chat/` — In-app messaging (coming soon)  
- `notifications/` — Alerts and activity tracking  
- `admin/` — Listing control & moderation  

---

## 📈 Future Enhancements

- 🔌 Real-time chat with sockets  
- 🧑‍🤝‍🧑 Referral & reward program  
- 📊 Usage analytics dashboard  
- 📱 Mobile app (React Native)  

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to fork, build, or contribute!

---

> 🧑‍💻 Developed by **Muzammil Haider** – 2025
