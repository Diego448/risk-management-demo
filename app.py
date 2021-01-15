from flask import Flask, render_template
from utils import Utils, get_total_risk
from db_utils import save_data

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
    dashboard_db.load()
    return render_template('dashboard.html', risk_score=get_total_risk(dashboard_db.data))

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
    risk = risk_db.get_registry(risk_id)
    print(risk_db.data)
    print(risk)
    return render_template('risk_details.html', risk=risk)

@app.route('/test')
def test():
    return "Hello from Docker environment"

@app.route('/test/db/<message>')
def db_test(message):
    data = {'message': message}
    result = save_data(data)
    return str(result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')