from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/execute-script', methods=['POST'])
def execute_script():
    try:
        data = request.get_json()
        url = data.get('url')
        selected_options = data.get('selectedOptions')

        # Run spamV3.py with the URL as an argument
        subprocess.run(['python', 'spamV3.py', url] + list(map(str, selected_options)))

        return jsonify({'message': 'Python script executed'})
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'message': f'Error executing script: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

