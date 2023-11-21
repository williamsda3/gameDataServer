from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


gameData = []
@app.route('/test', methods=['GET'])
def testing():
    return jsonify({'message': 'nice'})
@app.route('/getData', methods=['GET'])
def testing():
    return gameData

@app.route('/saveGameData', methods=['POST'])
def save_game_data():
    try:
        game_data = request.get_json()

        filename = 'gameData2.json'

        # Read existing data (if any)
        try:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append new game data
        existing_data.append(game_data)
        gameData.append(game_data)
        # Write back to the file
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=2)

        return jsonify({'success': True, 'message': 'Data saved successfully.' + str(game_data)}), 200
    except Exception as e:
        print(f"Error saving data: {e}")
        return jsonify({'success': False, 'message': 'Error saving data.'}), 500

if __name__ == '__main__':
    app.run(port=3000)
