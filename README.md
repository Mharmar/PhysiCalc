<div align="center">
<img src="./logo.png" alt="PhysiCalc Logo" width="200">
<h1>PhysiCalc API</h1>

<p>
<strong>A Robust, Modular, and Fully Tested Physics Calculation Engine</strong>
</p>

<p>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</a>
<a href="https://flask.palletsprojects.com/">
<img src="https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
</a>
<a href="https://docs.pytest.org/">
<img src="https://img.shields.io/badge/Testing-Pytest-yellow?style=for-the-badge&logo=pytest&logoColor=black" alt="Pytest">
</a>
<a href="https://render.com/">
<img src="https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</a>
</p>
</div>

<br />

🚀 Overview

PhysiCalc is a high-performance REST API designed to handle complex physics computations with precision. Built with a focus on robust error handling, input validation, and modularity, it serves as a reliable backend for physics simulation apps, educational tools, or scientific calculators.

The system features a strict Application Factory pattern using Flask Blueprints, ensuring that Electricity, Kinematics, Forces, and Projectile logic remain decoupled and scalable.

⚡ Key Features

🔌 Electricity Module

Ohm's Law: Calculate Voltage ($V$), Current ($I$), and Resistance ($R$).

Power Calculations: Compute Power ($P$) using flexible inputs ($V, I, R$).

Safety: Automatic zero-division protection for resistance checks.

🍎 Forces Module

Newtonian Mechanics: Normal Force, Tension, and Applied Force.

Friction: Static and Kinetic friction calculations ($F_f = \mu N$).

Non-Contact Forces: Gravitational and Electromagnetic force computations.

🏎️ Kinematics Module

SUVAT Equations: Solves for Velocity, Displacement, Time, and Acceleration.

Complex Handling: Handles squared velocity calculations safely.

🏹 Projectile Motion

Trajectory Analysis: Computes Max Height, Time of Flight, and Horizontal Range.

Trigonometry: Handles angular inputs automatically.

🔋 Work & Energy

Energy Systems: Kinetic Energy ($KE$) and Potential Energy ($PE$).

Work-Power: Calculates Work done and Power output over time.

📂 Project Structure

We utilize a clean, production-ready folder structure separating logic (formulas), routing (API), and validation (utils).

🛠️ Installation & Setup

Quick Start Guide

🧪 Testing

This project maintains high test coverage. Every route allows for:

Valid inputs (Happy Path).

Missing fields (400 Bad Request).

Invalid data types (String instead of Float).

Mathematical errors (Division by Zero).

To run the full suite:
pytest tests/

📡 API Usage Example

Endpoint: POST /api/kinematics/velocity

<div align="center">
<sub>Built with ❤️ by Mharmar</sub>
</div>