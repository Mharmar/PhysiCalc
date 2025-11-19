<div align="center">
<img src="./logo.png" alt="PhysiCalc Logo" width="200">
<h1>PhysiCalc API</h1>

<p>
<strong>A Robust, Modular, and Fully Tested Physics Calculation Engine</strong>
</p>

<p>
<a href="https://www.python.org/">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.12-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite" alt="Python">
</a>
<a href="https://flask.palletsprojects.com/">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Flask-3.0-black%3Fstyle%3Dfor-the-badge%26logo%3Dflask%26logoColor%3Dwhite" alt="Flask">
</a>
<a href="https://docs.pytest.org/">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Testing-Pytest-yellow%3Fstyle%3Dfor-the-badge%26logo%3Dpytest%26logoColor%3Dblack" alt="Pytest">
</a>
<a href="https://render.com/">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Deployed_on-Render-46E3B7%3Fstyle%3Dfor-the-badge%26logo%3Drender%26logoColor%3Dwhite" alt="Render">
</a>
</p>
</div>

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

PhysiCalc/
├── app/
│   ├── __init__.py           # App Factory & Blueprint Registration
│   ├── formulas/             # Pure Python Math Logic
│   │   ├── electricity.py
│   │   ├── forces.py
│   │   ├── kinematics.py
│   │   ├── projectile.py
│   │   └── work_energy.py
│   ├── routes/               # Flask API Endpoints
│   │   ├── electricity.py
│   │   ├── forces.py
│   │   ├── kinematics.py
│   │   ├── projectile.py
│   │   └── work_energy.py
│   └── utils/                # Core Utilities
│       ├── error_handler.py  # Standardized JSON Error Responses
│       └── validator.py      # Robust Input Validation
├── tests/                    # Comprehensive Test Suite (Pytest)
│   ├── test_electricity.py
│   ├── test_error_handling.py
│   ├── test_forces.py
│   ├── test_kinematics.py
│   ├── test_projectile.py
│   └── test_work_energy.py
├── run.py                    # Entry point
├── requirements.txt          # Dependencies
└── README.md                 # Documentation


🛠️ Installation & Setup

1. Clone the Repository

git clone [https://github.com/Mharmar/PhysiCalc.git](https://github.com/Mharmar/PhysiCalc.git)
cd PhysiCalc


2. Create a Virtual Environment

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Run Locally

On Windows (using Waitress):

waitress-serve --listen=*:8000 run:app


On Mac/Linux (using Gunicorn):

gunicorn run:app


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

Request Body:

{
  "u": 0,    // Initial Velocity
  "a": 9.8,  // Acceleration
  "t": 10    // Time
}


Success Response (200 OK):

{
  "formula": "v = u + a * t",
  "inputs": {
    "u": 0.0,
    "a": 9.8,
    "t": 10.0
  },
  "result": 98.0
}


Error Response (400 Bad Request):

{
  "error": "Invalid input"
}


<div align="center">
<sub>Built with ❤️ by Mharmar</sub>
</div>