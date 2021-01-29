from flask import Flask, render_template, request
app = Flask(_name_)

@app.route('/', methods=['GET'])
def index():
    return(render_template('index.html'))

@app.route('/', methods=['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']
    print(country1, country2, country3)
    datesCountry1 = getDates(country1)
    casesCountry1 = getCases(country1)
    deathsCountry1 = getDeaths(country1)
    print(datesCountry1)
    print(casesCountry1)
    print(deathsCountry1)
    return(render_template('index.html',datesCountry1=datesCountry1,casesCountry1=casesCountry1,deathsCountry1=deathsCountry1))

def getDates(country):
    listDates = ['11/11/2020','12/11/2020','13/11/2020','14/11/2020','15/11/2020','16/11/2020']
    return(listDates)
def getCases(country):
    listCases = [1, 10, 5, 7, 3, 8]
    return(listCases)
def getDeaths(country):
    listDeaths = [0, 1, 2, 7, 3, 4]
    return(listDeaths)
if _name=='main_':
    app.run(debug=True)