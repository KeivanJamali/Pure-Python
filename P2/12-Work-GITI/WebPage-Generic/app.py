import os

from flask import Flask, request, render_template, redirect, url_for, send_file, session
from DataLoader import Generic_DataLoader
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'K1ovn39nsfs49mlsg'  # Replace with a strong secret key

# Set your password here
PASSWORD = 'FaraGiti'

# Absolute paths
RAW_DATA_DIR = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-Generic\raw-data'
RESULT_DIR = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-Generic\result'
UPLOAD = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-Generic\uploads'
RAW_UPLOAD_DIR = r'D:\All Python\Pure-Python\P2\12-Work-GITI\WebPage-Generic\raw-upload'


def process_file(file, epsilon, roun_lim):
    # Ensure the result directory exists
    os.makedirs(RESULT_DIR, exist_ok=True)

    dataloader = Generic_DataLoader(file_name=file)
    dataloader.fit(epsilon=epsilon, round_lim=roun_lim)
    csv_file, txt_file, out_ranges_file, zeros_file = dataloader.save_file(RESULT_DIR)
    
    return csv_file, txt_file, out_ranges_file, zeros_file

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid password. Please try again.")
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        input_file = request.files['input_file']
        epsilon = float(request.form['epsilon'])
        roun_lim = float(request.form['roun_lim'])

        if input_file and epsilon and roun_lim:
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H-%M")
            folder_name = date_str
            new_filename = f"{input_file.filename.rsplit('.', 1)[0]}-{time_str}.{input_file.filename.rsplit('.', 1)[1]}"
            input_folder = os.path.join(UPLOAD, folder_name)
            os.makedirs(input_folder, exist_ok=True)
            input_filepath = os.path.join(input_folder, new_filename)
            input_file.save(input_filepath)
            
            csv_file, txt_file, out_ranges_file, zeros_file = process_file(input_filepath, epsilon, roun_lim)
            session['files'] = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
            
            return redirect(url_for('result'))
    
    return render_template('index.html')

@app.route('/result')
def result():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    files = session.get('files', [])
    return render_template('result.html', files=files)

@app.route('/list_raw_data')
def list_raw_data():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    raw_data_files = os.listdir(RAW_DATA_DIR)
    
    return render_template('list_raw_data.html', files=raw_data_files)


@app.route('/download_raw_data/<path:filename>')
def download_raw_data(filename):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    file_path = os.path.join(RAW_DATA_DIR, filename)
    
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"File '{filename}' not found in 'raw-data' directory."

@app.route('/download_result/<path:filename>')
def download_result(filename):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    file_path = os.path.join(RESULT_DIR, filename)
    
    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"File '{filename}' not found in 'result' directory."
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        upload_file = request.files['upload_file']
        if upload_file:
            upload_folder = RAW_UPLOAD_DIR
            os.makedirs(upload_folder, exist_ok=True)
            upload_filepath = os.path.join(upload_folder, upload_file.filename)
            upload_file.save(upload_filepath)
            return redirect(url_for('upload_success'))
    
    return render_template('upload.html')

@app.route('/upload_success')
def upload_success():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('upload_success.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
