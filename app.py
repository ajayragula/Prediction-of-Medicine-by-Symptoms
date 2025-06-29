from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to get medicine recommendations
def get_medicines(symptoms, age, history):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    recommended_medicines = []
    recommended_formulas = []

    for symptom in symptoms:
        cursor.execute("SELECT medicine, chemical_formula FROM medicines WHERE symptom=? AND medical_history IN (?, 'None')", (symptom.strip(), history))
        rows = cursor.fetchall()

        for row in rows:
            medicines = row[0].split(", ")
            formulas = row[1].split(", ")
            recommended_medicines.extend(medicines)
            recommended_formulas.extend(formulas)

    conn.close()

    return recommended_medicines, recommended_formulas

@app.route("/")
def home():
    return render_template("frontend.html")

@app.route('/predict', methods=['GET'])
def predict():
    symptoms = request.args.get('symptom', "").lower().split(',')
    age = int(request.args.get('age', 0))
    history = request.args.get('history', "None")

    medicines, formulas = get_medicines(symptoms, age, history)

    if medicines:
        return jsonify({"medicines": medicines, "formulas": formulas})
    else:
        return jsonify({"message": "No suitable medicine found. Please consult a doctor."})

if __name__ == '__main__':
    app.run(debug=True)