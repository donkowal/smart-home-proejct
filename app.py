from flask import Flask, render_template, request, jsonify
import functions  # import naszego pliku z funkcjami

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    button_number = data.get('button')

    # mapowanie numeru przycisku na funkcję
    func_map = {
        "1": functions.func1,
        "2": functions.func2,
        "3": functions.func3,
        "4": functions.func4
    }

    func_to_call = func_map.get(button_number)
    if func_to_call:
        message = func_to_call()
    else:
        message = "Nieznany przycisk!"

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
