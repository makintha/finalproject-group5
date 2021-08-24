#import Flask 
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import os


#################################################
# Database Setup
#################################################
path = os.path.dirname(os.path.abspath(__file__))
# print(path)
print(os.getcwd())

engine = create_engine(f"sqlite:///{path}/wells.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# print(Base.classes.keys())
# Save reference to the table
well7 = Base.classes.well_7
well8 = Base.classes.well_8
well9 = Base.classes.well_9
well10 = Base.classes.well_10
well15 = Base.classes.well_15
uni = Base.classes.uni_forecast
prod = Base.classes.production


#create an instance of Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multivariate')
def land_multi():
    return render_template('multivariate.html', coef = None)

@app.route('/plots')
def plot():
    return render_template('plots.html', coef = None)

### Multivariate
@app.route('/predict', methods=['GET','POST'])
def multivariate():
    
    if request.method == "POST":
        
        #get form data
        WaterRate = request.form.get('WaterRate')
        CasingHeadPressure = request.form.get('CasingHeadPressure')
        TubingHeadPressure = request.form.get('TubingHeadPressure')
        PumpSpeed = request.form.get('PumpSpeed')
        Torque = request.form.get('Torque')
        GasRate = request.form.get('GasRate')

        #call preprocessDataAndPredict and pass inputs
        try:
            prediction, coef = preprocessDataAndPredictLR(WaterRate, CasingHeadPressure, TubingHeadPressure, PumpSpeed, Torque, GasRate)
            #pass prediction to template
            # print(prediction)

            return render_template('multivariate.html', prediction = prediction[0], coef = coef)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass

### Univariate
# @app.route('/univariate/', methods=['GET','POST'])
# def univariate():
    
#     if request.method == "POST":
        
#         #get form data
#         Date = request.form.get('Date')
#         No_mos = request.form.get('No_of_months')
#         # TubingHeadPressure = request.form.get('TubingHeadPressure')
#         # PumpSpeed = request.form.get('PumpSpeed')
#         # Torque = request.form.get('Torque')
#         # GasRate = request.form.get('GasRate')

#         #call preprocessDataAndPredict and pass inputs
#         try:
#             prediction = preprocessDataAndPredictLTSM(Date, No_mos)
#             #pass prediction to template
#             return render_template('predict.html', prediction = prediction)
   
#         except ValueError:
#             return "Please Enter valid values"
  
#         pass
#     pass


###################### API ##########################

@app.route("/api/v1.0/Well7")
def Well7():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list well 7 data"""
    # Query all county data
    results = session.query(well7.Date, well7.actual, well7.forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, actual, forecast in results:
        well_7 = {}
        well_7["date"] = date
        well_7['actual'] = actual
        well_7['forecast'] = forecast
        all_data.append(well_7)

    return jsonify(all_data)

@app.route("/api/v1.0/Well8")
def Well8():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list well 8 data"""
    # Query all county data
    results = session.query(well8.Date, well8.actual, well8.forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, actual, forecast in results:
        well_8 = {}
        well_8["date"] = date
        well_8['actual'] = actual
        well_8['forecast'] = forecast
        all_data.append(well_8)

    return jsonify(all_data)

@app.route("/api/v1.0/Well9")
def Well9():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list well 9 data"""
    # Query all county data
    results = session.query(well9.Date, well9.actual, well9.forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, actual, forecast in results:
        well_9 = {}
        well_9["date"] = date
        well_9['actual'] = actual
        well_9['forecast'] = forecast
        all_data.append(well_9)

    return jsonify(all_data)

@app.route("/api/v1.0/Well10")
def Well10():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list well 10 data"""
    # Query all county data
    results = session.query(well10.Date, well10.actual, well10.forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, actual, forecast in results:
        well_10 = {}
        well_10["date"] = date
        well_10['actual'] = actual
        well_10['forecast'] = forecast
        all_data.append(well_10)

    return jsonify(all_data)


@app.route("/api/v1.0/Well15")
def Well15():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list well 15 data"""
    # Query all county data
    results = session.query(well15.Date, well15.actual, well15.forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, actual, forecast in results:
        well_15 = {}
        well_15["date"] = date
        well_15['actual'] = actual
        well_15['forecast'] = forecast
        all_data.append(well_15)

    return jsonify(all_data)

@app.route("/api/v1.0/univariate")
def uni_plot():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list forecast data"""
    # Query all county data
    results = session.query(uni.Date, uni.Forecast).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for date, forecast in results:
        univ = {}
        univ["date"] = date
        univ['forecast'] = forecast
        all_data.append(univ)

    return jsonify(all_data)

@app.route("/api/v1.0/prod")
def production():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list production data"""
    # Query all county data
    results = session.query(prod.Date, prod.Well,prod.WaterRate,prod.CasingHeadPressure,
    	prod.TubingHeadPressure, prod.PumpSpeed, prod.Torque, prod.GasRate).all()

    session.close()

    # # Create a dictionary from the row data and append to a list of all_precipitation
    all_data = []
    for d,w, wa, ca, tu, pu, to, ga in results: 
        prods = {}
        prods["date"] = d
        prods['well'] = w
        prods['waterrate'] = wa
        prods['casingheadpressure'] = ca
        prods['tubingheadpressure'] = tu
        prods['pumpspeed'] = pu
        prods['torque'] = to
        prods['gasrate'] = ga

        all_data.append(prods)

    return jsonify(all_data)



def preprocessDataAndPredictLR(WaterRate, CasingHeadPressure, TubingHeadPressure, PumpSpeed, Torque, GasRate):
    
    #keep all inputs in array
    test_data = [WaterRate, CasingHeadPressure, TubingHeadPressure, PumpSpeed, Torque, GasRate]
    print(test_data)
    
    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data)
    
    #open file
    file = open("LR_model.pkl","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    
    #predict
    prediction = trained_model.predict(test_data)

    # Coef
    coef = trained_model.coef_
    print(coef)
    return prediction, coef


def preprocessDataAndPredictLTSM(date, No_of_months):
    
    #keep all inputs in array
    test_data = [Date, No_of_months]
    print(test_data)
    
    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data)
    
    #open file
    file = open("univariate_predictions.h5","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    
    #predict
    prediction = trained_model.predict(test_data)
    
    return prediction
    
if __name__ == '__main__':
    # app.run(debug=True)
    app.debug=True
    app.run()

    