from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('nb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the feature columns
feature_columns = ['Src IP dec','Src Port','Dst IP dec','Dst Port','Protocol','Flow Duration','Total Fwd Packet','Total Bwd packets','Total Length of Fwd Packet','Total Length of Bwd Packet','Fwd Packet Length Max','Fwd Packet Length Min']

@app.route('/')
def home():
    return render_template('index.html', columns=feature_columns)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    for key in data:
        data[key] = float(data[key])
    
    input_data = pd.DataFrame([data], columns=feature_columns)
    prediction = model.predict(input_data)
    print(prediction)
    
    output = prediction[0]
    
    return render_template('index.html', prediction_text=f'The network traffic is {output}', columns=feature_columns)

if __name__ == "__main__":
    app.run(debug=True)
