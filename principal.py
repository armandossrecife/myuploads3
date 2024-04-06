from flask import Flask, render_template, send_from_directory
from app.controllers.dashboard import dashboard_bp
from app.controllers.uploads import uploads_bp
import os

app = Flask(__name__, template_folder='app/templates')

STATIC_PATH = os.path.join(app.root_path, 'app/static')
app.secret_key = 'thisismysecretkeyfrommywebapplication'  # Replace with a strong secret key
app.static_folder = STATIC_PATH

# Register Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(uploads_bp)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(STATIC_PATH, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def hello():
    print('Bem vindo ao Flask!')        
    print('Lista de recursos disponíveis da aplicação MyUpload: ')
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = str(rule.endpoint) + ' - '+ str(methods) + ' - '+ str(rule)
        output.append(line)

    for line in sorted(output):
        print(line)

    return render_template("dashboard/index.html")

if __name__ == '__main__':
    app.run(debug=True)