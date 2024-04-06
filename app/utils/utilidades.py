import os

# Todo: checar os diretorios uploads e thumbnails
class Constant:
    PATH_MYADMIN = os.path.abspath(os.getcwd())
    PATH_MYAPP = PATH_MYADMIN + '/app'
    PATH_STATIC = PATH_MYADMIN + '/app/static'
    PATH_UPLOADS = PATH_MYADMIN + '/app/static/uploads'
    PATH_UPLOADS_THUMBNAILS = PATH_MYADMIN + '/app/static/uploads/thumbnails'
    PATH_UPLOADS_S3 = 'https://my-app-image-bucket.s3.amazonaws.com'