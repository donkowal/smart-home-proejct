from flask import Flask, render_template, request, jsonify
import functions  # import naszego pliku z funkcjami
import scenes

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
        "1": scenes.TV,
        "2": scenes.Projektor,
        "3": scenes.All_off,
        "4": functions.Klima_on_off,
    }

    func_to_call = func_map.get(button_number)
    if func_to_call:
        message = func_to_call()
        print("wywołano")
    else:
        message = "Nieznany przycisk!"

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

