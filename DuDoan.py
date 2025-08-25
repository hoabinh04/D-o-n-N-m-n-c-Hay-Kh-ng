from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load model
try:
    with open("mushroom_model.pkl", "rb") as f:
        tree = pickle.load(f)
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file mushroom_model.pkl")
    exit(1)

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "Không xác định"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_mushroom():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["odor", "cap-color", "gill-color"]):
            return jsonify({"error": "Vui lòng cung cấp đầy đủ thông tin!"}), 400

        sample = {
            "odor": data["odor"],
            "cap-color": data["cap-color"],
            "gill-color": data["gill-color"]
        }

        prediction = predict(tree, sample)

        if prediction == "e":
            result = "🍄 Nấm ăn được (Edible)"
        elif prediction == "p":
            result = "☠️ Nấm độc (Poisonous)"
        else:
            result = "⚠️ Không xác định được"

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": f"Lỗi server: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
