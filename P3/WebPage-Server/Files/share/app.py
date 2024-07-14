from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session, send_file
import os
from werkzeug.utils import secure_filename
from Generic_DataLoader import Generic_DataLoader
from PPK_Processing import PPK_Processing_Result_DataLoader

app = Flask(__name__)
app.config['UPLOAD_FOLDER_SEND'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\send_to_others'
app.config['UPLOAD_FOLDER_RECEIVED'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\received_from_others'
app.config['UPLOAD_FOLDER_SHARE'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\share'
app.config['RESULT_DIR'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\result'
app.secret_key = 'supersecretkey'
passwords = {"Generic_Processing": "1234",
             "PPK_Processing": "1234",
             "Connect": "asdf1234"}

@app.route('/')
def index():
    items = ['Receive Files from Me', 'Upload Files to Me', 'Share Files', 'Generic Processing', 'PPK Processing']
    return render_template('index.html', items=items)

def handle_file_download(folder, filename=None):
    if filename:
        file_path = os.path.join(folder, filename)
        return send_file(file_path, as_attachment=True)
    else:
        files = os.listdir(folder)
        return render_template('download.html', files=files)

@app.route('/download', defaults={'filename': None})
@app.route('/download/<filename>')
def download_file(filename):
    return handle_file_download(app.config['UPLOAD_FOLDER_SEND'], filename)

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

@app.route('/share', methods=['GET', 'POST'], defaults={'filename': None})
@app.route('/share/<filename>')
def share_files(filename):
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['Connect']:
            pass
        else:
            flash('Incorrect password')
            return redirect(url_for('share_files'))

    # if request.method == 'POST':
        # Handle file upload
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        if not files or all(file.filename == '' for file in files):
            flash('No selected file')
            return redirect(request.url)
        upload_folder = app.config['UPLOAD_FOLDER_SHARE']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        for file in files:
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_folder, filename))
        flash('Files successfully uploaded')
        return redirect(url_for('share_files'))

    # Handle file download
    if filename:
        return handle_file_download(app.config['UPLOAD_FOLDER_SHARE'], filename)
    else:
        files = os.listdir(app.config['UPLOAD_FOLDER_SHARE'])
        return render_template('share.html', files=files)
    
@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['Connect']:
            return redirect(url_for('connect_page'))
        else:
            flash('Incorrect password')
    return render_template('connect.html')

@app.route('/connect_page')
def connect_page():
    send_files = os.listdir(app.config['UPLOAD_FOLDER_SEND'])
    return render_template('connect_page.html', send_files=send_files)
    
@app.route('/results', defaults={'filename': None})
@app.route('/results/<filename>')
def results(filename):
    if filename:
        return handle_file_download(app.config['RESULT_DIR'], filename)
    else:
        files = session.get('files', [])
        return render_template('result.html', files=files)

def generic_process_file(file, epsilon, roun_lim):
    dataloader = Generic_DataLoader(file_name=file)
    dataloader.fit(epsilon=epsilon, round_lim=roun_lim)
    csv_file, txt_file, out_ranges_file, zeros_file = dataloader.save_file(app.config['RESULT_DIR'])
    return csv_file, txt_file, out_ranges_file, zeros_file

@app.route('/generic_processing', methods=['GET', 'POST'])
def generic_processing():
    def process(file, epsilon, roun_lim):
        dataloader = Generic_DataLoader(file_name=file)
        dataloader.fit(epsilon=epsilon, round_lim=roun_lim)
        csv_file, txt_file, out_ranges_file, zeros_file = dataloader.save_file(app.config['RESULT_DIR'])
        return csv_file, txt_file, out_ranges_file, zeros_file
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['Generic_Processing']:
            file = request.files['file']
            epsilon = float(request.form['epsilon'])
            rounding_limit = float(request.form['rounding_limit'])
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['RESULT_DIR'], filename)
                file.save(file_path)
                # Process the file
                csv_file, txt_file, out_ranges_file, zeros_file = process(file_path, epsilon, rounding_limit)
                result_files = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                session['files'] = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                result_url = url_for('results', files=result_files)
                return {'result_url': result_url}
        else:
            flash('Incorrect password')
            return redirect(url_for('generic_processing'))
    return render_template('generic_process.html')

@app.route('/PPK_processing', methods=['GET', 'POST'])
def PPK_processing():
    def process(file):
        dataloader = PPK_Processing_Result_DataLoader(file_name=file)
        PPK_file = dataloader.save(app.config['RESULT_DIR'])
        return PPK_file
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['PPK_Processing']:
            file = request.files['file']
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['RESULT_DIR'], filename)
                file.save(file_path)
                # Process the file
                PPK_file, empty_file, text_files = process(file_path)
                text_files = [os.path.basename(filee) for filee in text_files]
                result_files = [os.path.basename(PPK_file), os.path.basename(empty_file)] + text_files
                session['files'] = [os.path.basename(PPK_file), os.path.basename(empty_file)] + text_files
                result_url = url_for('results', files=result_files)
                return {'result_url': result_url}
        else:
            flash('Incorrect password')
            return redirect(url_for('PPK_processing'))
    return render_template('PPK_process.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
