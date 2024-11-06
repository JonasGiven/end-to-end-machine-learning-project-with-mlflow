from flask import Flask, render_template, request, url_for
import os 
import numpy as np
import pandas as pd
from src.mlproject.pipeline.prediction import PredictionPipeline

app = Flask(__name__, static_folder='Static') # initializing a flask app

@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])
def training():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        main_script = os.path.join(current_dir, "main.py")
        if os.path.exists(main_script):
            os.system(f"python {main_script}")
            return "Training Successful!"
        else:
            return "Error: main.py not found. Please check if main.py exists in the same directory as app.py"
    except Exception as e:
        return f"Error during training: {str(e)}"
    
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)   #storing the data inserted by user
            
            obj = PredictionPipeline()
            predict = obj.predict(data)   #make a prediction

            return render_template('results.html', prediction = str(predict))  #return under result.html

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    #app.run(port=5000, debug=True)
    app.run(port=5000)