from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Hydrological Surveys',
        'amount': 'Ksh'
    },
    {
        'id': 2,
        'title':'Boreholes Drilling',
        'amount': 'Ksh'
    },
    {
        'id': 3,
        'title':'Boreholes Equipping and Maintenace',
        'amount': 'Ksh'
    },
    {
        'id': 4,
        'title':'Boreholes Solarizations and Solar backups', 
        'amount': 'Ksh'
    },
    {
        'id': 5,
        'title':'Water Purification',
        'amount':'Ksh'
    },
    {
        'id': 6,
        'title':'Borehole works(All)', 
        'amount':'Ksh'
    }
]

@app.route("/")
def hello_confined():
    return render_template('home.html', jobs=JOBS)


if __name__== "__main__":
    app.run(host="0.0.0.0",debug= True)
