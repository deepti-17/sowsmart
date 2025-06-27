from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

# Load model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Detect if request is from app (JSON) or website (form)
        if request.is_json:
            data = request.get_json()
            N = float(data["Nitrogen"])
            P = float(data["Phosporus"])
            K = float(data["Potassium"])
            temp = float(data["Temperature"])
            humidity = float(data["Humidity"])
            ph = float(data["Ph"])
            rainfall = float(data["Rainfall"])
        else:
            N = float(request.form['Nitrogen'])
            P = float(request.form['Phosporus'])
            K = float(request.form['Potassium'])
            temp = float(request.form['Temperature'])
            humidity = float(request.form['Humidity'])
            ph = float(request.form['Ph'])
            rainfall = float(request.form['Rainfall'])

        features = [N, P, K, temp, humidity, ph, rainfall]
        scaled = ms.transform([features])
        final = sc.transform(scaled)
        prediction = model.predict(final)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction[0], "Unknown Crop")
        result = f"{crop} is the best crop to be cultivated right there"

        if request.is_json:
            return jsonify({"result": result})
        else:
            return render_template("index.html", result=result)

    except Exception as e:
        if request.is_json:
            return jsonify({"error": str(e)})
        else:
            return render_template("index.html", result=f"Error in prediction: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
