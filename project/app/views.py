from flask import render_template, redirect
from app import app
from app.forms import LoginForm
from app.plot import plot
import pandas as pd

DATA = pd.read_csv('data/prototype_ready.csv', sep=';', encoding='cp1251')

@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/find', methods = ['GET', 'POST'])
def login():
    global Form
    Form = LoginForm()
    if Form.validate_on_submit():
        return redirect('/answer')
    return render_template('find.html', 
        title = 'Sign In',
        form = Form)

@app.route('/answer', methods = ['GET', 'POST'])
def answer():
    street = Form.street.data.strip()
    house = Form.house.data
    building = int(Form.building.data)
    letter = Form.letter.data
    answer = DATA[(DATA.addr_street==street)&(DATA.addr_number==house)&
        (DATA.addr_building==building)&(DATA.addr_letter==letter)]
    name = answer.to_dict('record')[0]['number']
    plot(answer, name)
    return render_template('answer.html', 
        street = street,
        house = house,
        building = building,
        letter = letter,
        addr_district = answer.to_dict('record')[0]['addr_district'],
        data_buildingdate = answer.to_dict('record')[0]['data_buildingdate'],
        param_ukname = answer.to_dict('record')[0]['param_ukname'],
        repair_years = answer.to_dict('record')[0]['repair_years'],
        repair_work_problem = answer.to_dict('record')[0]['repair_work_problem'],
        name = '/static/' + str(name) + '.png',
        lat = answer.to_dict('record')[0]['lat'],
        lon = answer.to_dict('record')[0]['lon'])