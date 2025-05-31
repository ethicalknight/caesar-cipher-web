# 🔐 Caesar Cipher Web App

A simple but modern web application for encrypting and decrypting messages using the **Caesar Cipher algorithm**, built with **Python (Flask)** and styled using **HTML, CSS, and Bootstrap**.

 🛠 Features

- 🔁 **Auto Encrypt & Decrypt**  
  - Encrypts text with a random shift
  - Decrypts automatically if input is in the encrypted format (`ENC:<shift>::<message>`)

- 💻 **User-Friendly Interface**  
  - Clean, responsive UI using Bootstrap  
  - Dark theme for modern look

- 📁 **Saves output to file**  
  - Output stored in `output/result.txt`

- 💡 Beginner-friendly Python + Web Dev project

---

## ⚙️ How It Works

### Encryption Flow:

- User enters a message
- App uses a random shift (1-25) to encrypt it
- Returns output like: `ENC:7::Olssv dvysk`

### Decryption Flow:

- User pastes an encrypted message like: `ENC:7::Olssv dvysk`
- App detects format and auto-decrypts it

---

## 🧩 Technologies Used

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML + CSS (Bootstrap)
- Jinja2 (for rendering HTML templates)
