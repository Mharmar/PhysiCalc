<div align="center">
  <img src="./logo.png" alt="PhysiCalc Logo" width="200">

  <h1>PhysiCalc API</h1>
  <p><strong>A Modular Physics Computation API built with Flask</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
    <img src="https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask">
    <img src="https://img.shields.io/badge/Pillow-Image%20Gen-orange?style=for-the-badge&logo=python">
    <img src="https://img.shields.io/badge/Render-Deployment-purple?style=for-the-badge&logo=render">
    <img src="https://img.shields.io/badge/PyTest-Testing-green?style=for-the-badge&logo=pytest">
  </p>
</div>

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
  <img src="./img_structure.png" width="750">
</div>

---

## 🛠 Installation & Setup

Here’s the installation guide image generated using your Pillow script:

<div align="center">
  <img src="./img_install.png" width="750">
</div>

---

## 📡 API Usage Example

This is the example request/response for kinematics (velocity):

<div align="center">
  <img src="./img_usage.png" width="750">
</div>

---

## 🧠 Modules Included

### ⚡ Electricity
- Ohm’s Law (V, I, R)  
- Power equations  
- Auto-handles division-by-zero  

### 🏎️ Kinematics
- Full SUVAT equations  
- Velocity, displacement, acceleration, time  
- Proper input validation  

### 🏹 Projectile Motion
- Range  
- Time of flight  
- Maximum height  
- Angle → radians conversion handled internally  

### 🔋 Work & Energy
- Kinetic & Potential energy  
- Work  
- Power  

### 🍎 Forces
- Net force  
- Weight (gravity)  
- Friction  
- Normal force  

---

## 🧪 Testing  
(Unit tests folder is prepared at `/tests/`)

Run tests:

```bash
pytest tests/

