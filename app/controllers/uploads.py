from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.utils.utilidades import Constant
import os

uploads_bp = Blueprint('upload', __name__, template_folder='app/templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@uploads_bp.route('/upload', methods=['GET'])
def upload_form():
    return render_template('uploads/upload.html')

@uploads_bp.route('/upload', methods=['POST'])
def upload_image():
    # Checa se o file pick foi selecionado com um arquivo
    if 'file' not in request.files:
        flash('Arquivo sem conteúdo!')
        return redirect(request.url)

    file = request.files['file']
    # Checa se o file name esta vazio
    if file.filename == '':
        flash('Arquivo não selecionado!')
        return redirect(request.url)

    # Garante que existe um arquivo selecionado e o tipo de arquivo e valido
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Salva o arquivo na pasta de uploads
        file.save(os.path.join(Constant.PATH_UPLOADS, filename))
        flash('Upload da imagem realizado com sucesso!')
        return redirect(url_for('upload.uploaded_images'))
    else:
        flash('Tipos de imagens permitidos: png, jpg, jpeg, gif')
        return redirect(request.url)

@uploads_bp.route('/imagens/<filename>')
def uploaded_file(filename):
    return send_from_directory(Constant.PATH_UPLOADS, filename)

# Retorna uma pagina contendo a lista de imagens que foram uploaded
@uploads_bp.route('/imagens')
def uploaded_images():
    images = os.listdir(Constant.PATH_UPLOADS)
    return render_template('uploads/uploaded_images.html', images=images)