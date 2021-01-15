docker run -p 5000:5000 \ 
-w /risk-management-demo \
 -v "$(pwd):/risk-management-demo" \ 
 python:3.8-buster \ 
 bash -c "python3 -m pip install flask && export FLASK_APP=app.py && export FLASK_ENV=development && python -m flask run --host 0.0.0.0"