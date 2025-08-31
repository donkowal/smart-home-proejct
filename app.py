from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    button_number = data.get('button')
    return jsonify({"message": f"Kliknąłeś przycisk {button_number}!"})

if __name__ == '__main__':
    app.run(debug=True)
