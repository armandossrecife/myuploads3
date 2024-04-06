from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.utils.utilidades import Constant
import os
import boto3

uploads_bp = Blueprint('upload', __name__, template_folder='app/templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Configure S3 access (replace with your credentials and bucket name)
s3 = boto3.client(
    's3',
    aws_access_key_id='?',
    aws_secret_access_key='?'
)
bucket_name = 'my-app-image-bucket'

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
        # Salva o arquivo no bucket de imagens da aplicacao
        s3.upload_fileobj(file, bucket_name, filename)
        flash('Upload da imagem realizado com sucesso!')
        return redirect(url_for('upload.list_all_images_from_bucket'))
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

def list_bucket_images(bucket_name):
  response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=20)
  image_names = []
  for obj in response.get('Contents', []):
    # Extract filename from 'Key' attribute
    filename = obj['Key']
    print(filename)
    image_names.append(filename)
    return image_names

@uploads_bp.route('/imagenss3/<filename>')
def uploaded_file_s3(filename):
    return send_from_directory(Constant.PATH_UPLOADS_S3, filename)

@uploads_bp.route('/imagess3')
def list_all_images_from_bucket():
    print('Lista todas as imagens do bucket corrente')
    image_names = list_bucket_images(bucket_name)
    print(image_names)
    lista_urls_imagens = []
    for image in image_names:
        url = Constant.PATH_UPLOADS_S3 + '/' + image
        lista_urls_imagens.append(url)

    return render_template('uploads/uploaded_images_s3.html', images=lista_urls_imagens)