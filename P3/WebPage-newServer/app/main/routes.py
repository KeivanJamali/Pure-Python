from flask import render_template, redirect, url_for, flash, session, send_file, request
import os
from werkzeug.utils import secure_filename
from app.main import bp
from app import create_app

app = create_app()

@bp.route('/')
def index():
    items = ['Receive Files from Me', 'Upload Files to Me', 'Share Files', 'Generic Processing']
    return render_template('index.html', items=items)

@bp.route('/download')
def download_files():
    files = os.listdir(app.config['UPLOAD_FOLDER_SEND'])
    return render_template('download.html', files=files)

@bp.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER_SEND'], filename)
    return send_file(file_path, as_attachment=True)

@bp.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        if not files or all(file.filename == '' for file in files):
            flash('No selected file')
            return redirect(request.url)
        upload_folder = app.config['UPLOAD_FOLDER_RECEIVED']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        for file in files:
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_folder, filename))
        flash('Files successfully uploaded')
        return redirect(url_for('main.upload_files'))
    return render_template('upload.html')
