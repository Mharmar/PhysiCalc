<div align="center">
  <img src="./assets/logo.png" alt="PhysiCalc Logo" width="200">

  <h1>PhysiCalc API</h1>
  <p><strong>A Modular Physics Computation API built with Flask</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
    <img src="https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask">
    <img src="https://img.shields.io/badge/Pillow-Image%20Gen-orange?style=for-the-badge&logo=python">
    <img src="https://img.shields.io/badge/Render-Deployment-purple?style=for-the-badge&logo=render">
    <img src="https://img.shields.io/badge/PyTest-Testing-green?style=for-the-badge&logo=pytest">
    <img src="https://img.shields.io/badge/Swagger-API%20Docs-blue?style=for-the-badge&logo=swagger">
  </p>
</div>

---

## 🚀 Overview

PhysiCalc is a **physics engine API** built using Flask and designed for:

- Educational tools  
- Physics calculators  
- Simulation backends  
- Mobile/desktop apps needing physics computation  

It provides modular calculation engines for:

- Kinematics  
- Projectile Motion  
- Work & Energy  
- Electricity  
- Forces  

All formulas are isolated inside `app/formulas/`, while API endpoints live inside `app/routes/`.

---

## 📂 Project Structure

Below is the auto-generated visual file structure:

<div align="center">
  <img src="./assets/img_structure.png" width="750">
</div>

---

## 🛠 Installation & Setup

Here’s the installation guide image generated using your Pillow script:

<div align="center">
  <img src="./assets/img_install.png" width="750">
</div>

### Install dependencies

```bash
pip install -r requirements.txt
````

Requirements include:

```
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
pytest==8.0.0
flasgger==0.9.7.1
Pillow
```

---

## 📡 API Usage Example

This is the example request/response for kinematics (velocity):

<div align="center"> <img src="./assets/img_usage.png" width="750"> </div>

---

## 📘 API Documentation (Swagger / Flasgger)

PhysiCalc includes automatic API documentation via Flasgger.

Live docs:
👉 [https://physicalc.onrender.com/apidocs/](https://physicalc.onrender.com/apidocs/)

Features:

* Auto-generated Swagger UI
* Test endpoints directly
* Faster frontend/mobile integration

---

## 🧠 Modules Included

### ⚡ Electricity

* Ohm’s Law (V, I, R)
* Power equations
* Auto-handles division-by-zero

### 🏎️ Kinematics

* Full SUVAT equations
* Velocity, displacement, acceleration, time
* Proper input validation

### 🏹 Projectile Motion

* Range
* Time of flight
* Maximum height
* Angle → radians conversion handled internally

### 🔋 Work & Energy

* Kinetic & Potential energy
* Work
* Power

### 🍎 Forces

* Net force
* Weight (gravity)
* Friction
* Normal force

---

## 🧪 Testing

Unit tests are located in `/tests/`.

Run tests:

```bash
pytest
```

---

## 🌍 Deployment (Render)

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn run:app
```

Live deployment:
👉 [https://physicalc.onrender.com/apidocs/#](https://physicalc.onrender.com/apidocs/#)

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 👨‍💻 Author

Made by Mhar with ❤️ and Python.

```
```
