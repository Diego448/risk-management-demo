from flask import Flask, render_template
from utils import Utils

app = Flask(__name__)
risk_db = Utils('data/risks.json')
dashboard_db = Utils('data/dashboard_risks.json')

@app.route('/')
def welcome_page():
    return render_template('welcome.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/dashboard/risks')
def dashboard_risks():
    dashboard_db.load()
    return render_template('dashboard_risks.html', risks=dashboard_db.data)

@app.route('/risks/all')
def risks():
    risk_db.load()
    return render_template('risks.html', risks=risk_db.data)

@app.route('/risks/<risk_id>')
def risk_details(risk_id):
    return render_template('risk_details.html')