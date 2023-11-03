## This server will do multiple things
# 1. Route packets to servers from clients
# 2. Host the webapp that will monitor the traffic and routing
# 3. (Just a joke) Occasionally send the mp3 file for "'I Was Made For Lovin You' By KISS'" to all servers
from flask import Flask, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend/build', template_folder='../frontend/build')
CORS(app)  # Enable CORS

@app.route('/Home', defaults={'path': ''})
@app.route('/Home/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

# Catch all other paths to allow for client-side routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
if __name__ == '__main__':
    app.run(debug=True)

