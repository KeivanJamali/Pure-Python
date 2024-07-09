from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session, send_file
import os
from werkzeug.utils import secure_filename
from Generic_DataLoader import Generic_DataLoader

app = Flask(__name__)
app.config['UPLOAD_FOLDER_SEND'] = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-FaraGiti\Files\send_to_others'
app.config['UPLOAD_FOLDER_RECEIVED'] = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-FaraGiti\Files\received_from_others'
app.config['UPLOAD_FOLDER_SHARE'] = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-FaraGiti\Files\share'
app.config['RESULT_DIR'] = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-FaraGiti\Files\result'
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    items = ['Receive Files from Me', 'Upload Files to Me', 'Share Files', 'Generic Processing']
    return render_template('index.html', items=items)

@app.route('/download')
def download_files():
    files = os.listdir(app.config['UPLOAD_FOLDER_SEND'])
    return render_template('download.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER_SEND'], filename)
    return send_file(file_path, as_attachment=True)

@app.route('/upload', methods=['GET', 'POST'])
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
        return redirect(request.url)
    return render_template('index.html')

@app.route('/share', methods=['GET', 'POST'])
def share_files():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_SHARE'], filename))
            flash('File successfully uploaded')
            return redirect(request.url)
    files = os.listdir(app.config['UPLOAD_FOLDER_SHARE'])
    return render_template('share.html', files=files)

@app.route('/share/download/<filename>')
def share_download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER_SHARE'], filename)

def generic_process_file(file, epsilon, roun_lim):
    dataloader = Generic_DataLoader(file_name=file)
    dataloader.fit(epsilon=epsilon, round_lim=roun_lim)
    csv_file, txt_file, out_ranges_file, zeros_file = dataloader.save_file(app.config['RESULT_DIR'])
    return csv_file, txt_file, out_ranges_file, zeros_file

@app.route('/generic_processing', methods=['GET', 'POST'])
def generic_processing():
    if request.method == 'POST':
        password = request.form['password']
        if password == '1234':  # Use a secure password management system in production
            file = request.files['file']
            epsilon = float(request.form['epsilon'])
            rounding_limit = float(request.form['rounding_limit'])
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['RESULT_DIR'], filename)
                file.save(file_path)
                # Process the file
                csv_file, txt_file, out_ranges_file, zeros_file = generic_process_file(file_path, epsilon, rounding_limit)
                result_files = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                session['files'] = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                result_url = url_for('show_results', files=result_files)
                return {'result_url': result_url}
        else:
            flash('Incorrect password')
            return redirect(url_for('generic_processing'))
    return render_template('generic_process.html')

@app.route('/results')
def show_results():
    files = request.args.getlist('files')
    return render_template('generic_result.html', files=files)

@app.route('/results/download/<filename>')
def download_result_file(filename):
    file_path = os.path.join(app.config["RESULT_DIR"], filename)
    
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"File '{filename}' not found in 'raw-data' directory."

@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'K1':  # Use a secure password management system in production
            return redirect(url_for('connect_page'))
        else:
            flash('Incorrect password')
    return render_template('connect.html')

@app.route('/connect_page')
def connect_page():
    send_files = os.listdir(app.config['UPLOAD_FOLDER_SEND'])
    return render_template('connect_page.html', send_files=send_files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
