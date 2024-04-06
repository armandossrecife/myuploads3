from flask import Blueprint
from flask import render_template

dashboard_bp = Blueprint('dashboard', __name__, template_folder='app/templates')

@dashboard_bp.route('/dashboard')
def dashboard_page():
    print('Carrega o dashboard da aplicação')
    
    return render_template("dashboard/index.html")