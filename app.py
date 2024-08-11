from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    folder_names = os.listdir('data')
    folder_names = [f for f in folder_names if os.path.isdir(os.path.join('data', f))]
    return render_template('index.jinja', folders=folder_names)

@app.route('/get_images/<folder_name>', methods=['GET'])
def get_images(folder_name):
    folder_path = os.path.join('data', folder_name)
    if not os.path.exists(folder_path):
        return jsonify([]), 404
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    image_files.sort()  # Ensure the images are sorted
    return jsonify(image_files)

@app.route('/data/<path:filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('data', filename)

if __name__ == '__main__':
    app.run(debug=True)
