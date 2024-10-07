from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from Generic_DataLoader_V4 import Generic_DataLoader
from PPK_Processing_V1 import PPK_Processing_Result_DataLoader
from CSDP_DataLoader import CSDP_DataLoader
from Delete_distance_from_centerline import Delete_Distance_From_Centerline
from assistant_V1 import send_to_assistant, context
import pandas as pd
from datetime import datetime

# r'/home/Keivan01/mysite/Files/send_to_others'
app = Flask(__name__)
app.config['UPLOAD_FOLDER_SEND'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\send_to_others'
app.config['UPLOAD_FOLDER_RECEIVED'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\received_from_others'
app.config['UPLOAD_FOLDER_SHARE'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\share'
app.config['RESULT_DIR'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\result'
app.config['MOVIE_FOLDER'] = r'D:\All Python\Pure-Python\P3\WebPage-Server\Files\share'
app.config['APP_FOLDER'] = r"D:\All Python\Pure-Python\P3\WebPage-Server\Files\apps"
app.config['STATISTIC'] = r"D:\All Python\Pure-Python\P3\WebPage-Server\Files\statistic"
app.secret_key = 'supersecretkey'
passwords = {"Generic_Processing": "1234",
             "PPK_Processing": "1234",
             "CSDP_Processing": "1234",
             "Connect": "asdf1234",
             "Image_Processing": "1234",
             "Delete_empty_processing": "1234",
             "culvert_desing": "1234"}

items = ['Connect to Me', 'Share Files', 'Generic Processing', 'PPK Processing', 'CSDP Processing', 'Image Processing',
         'Delete Empty Processing', 'Culvert Processing', 'Chat-GPT']

def initialize_history_version():
    # List all history files
    existing_files = [f for f in os.listdir(app.config['STATISTIC']) if f.startswith('history_V') and f.endswith('.csv')]
    
    # Extract version numbers from filenames
    if existing_files:
        max_version = max(int(f.split('_V')[1].split('.csv')[0]) for f in existing_files)
    else:
        max_version = -1  # If no files exist, start from -1

    return max_version
            
def add_to_history(name, logged_in):
    file = app.config['STATISTIC']+f"/history_V{initialize_history_version()}.csv"
    if logged_in == 0:
        logged_in = "Logged-in Properly"
    elif logged_in == 1:
        logged_in = "Password Incorrect"
    elif logged_in == 2:
        logged_in = "Bad inputs"
    elif logged_in == 3:
        logged_in = name
    try:
        data = pd.read_csv(file, index_col=0)
        if len(data.columns) != len(items)+4:
            raise
    except:
        data = pd.DataFrame(0, index=range(1), columns=["Date", "IP Address", "logged-in"]+items+["Downloads"])
        file = app.config['STATISTIC']+f"/history_V{initialize_history_version()+1}.csv"
    
    if name == 'Connect to Me':
        r = 1
    elif name == 'Share Files':
        r = 2
    elif name == 'Generic Processing':
        r = 3
    elif name == 'PPK Processing':
        r = 4
    elif name == 'CSDP Processing':
        r = 5
    elif name == 'Image Processing':
        r = 6
    elif name == 'Delete Empty Processing':
        r = 7
    elif name == 'Culvert Processing':
        r = 8
    elif name == 'Chat-GPT':
        r = 9
    else:
        r = 10

    new_row = [datetime.now().strftime("%Y/%m/%d | %H:%M:%S"), request.remote_addr, logged_in] + [1 if _ == r else 0 for _ in range(1, len(items)+1)] + [1 if r==10 else 0]
    data.loc[len(data)] = new_row
    data.iloc[0, 3:] = data.iloc[1:, 3:].sum().values
    data.iloc[0, :3] = len(data) - 1
    data.to_csv(file)

@app.route('/')
def index():
    return render_template('index.html', items=items)

def handle_file_download(folder, filename=None):
    if filename:
        file_path = os.path.join(folder, filename)
        return send_file(file_path, as_attachment=True)
    else:
        files = os.listdir(folder)
        return render_template('download.html', files=files)

@app.route('/download', defaults={'filename': None, 'folder': None})
@app.route('/download/<folder>/<filename>')
def download_file(filename, folder):
    add_to_history(name=filename, logged_in=3)
    return handle_file_download(app.config[folder], filename)

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
            add_to_history(name="Share Files", logged_in=0)
        else:
            add_to_history(name="Share Files", logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('share_files'))

    if request.method == 'POST':
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
        return download_file('UPLOAD_FOLDER_SHARE', filename)
    else:
        files = os.listdir(app.config['UPLOAD_FOLDER_SHARE'])
        return render_template('share.html', files=files)
    
@app.route('/connect', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['Connect']:
            add_to_history(name="Connect to Me", logged_in=0)
            return redirect(url_for('connect_page'))
        else:
            add_to_history(name="Connect to Me", logged_in=1)
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
        return download_file(filename, 'RESULT_DIR')
    else:
        files = session.get('files', [])
        return render_template('result.html', files=files)


@app.route('/generic_processing', methods=['GET', 'POST'])
def generic_processing():
    def process(file, epsilon, roun_lim):
        dataloader = Generic_DataLoader(file_name=file)
        dataloader.fit(epsilon=epsilon, round_lim=roun_lim)
        csv_file, txt_file, out_ranges_file, zeros_file = dataloader.save_files(app.config['RESULT_DIR'])
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
                try:
                    csv_file, txt_file, out_ranges_file, zeros_file = process(file_path, epsilon, rounding_limit)
                    result_files = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                    session['files'] = [os.path.basename(csv_file), os.path.basename(txt_file), os.path.basename(out_ranges_file), os.path.basename(zeros_file)]
                    result_url = url_for('results', files=result_files)
                    add_to_history(name='Generic Processing', logged_in=0)
                    return {'result_url': result_url}
                except:
                    add_to_history(name='Generic Processing', logged_in=2)
                    flash('Wrong Inputs.')
                    return redirect(url_for('generic_processing'))
        else:
            add_to_history(name='Generic Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('generic_processing'))
    return render_template('generic_process.html')

@app.route('/PPK_processing', methods=['GET', 'POST'])
def PPK_processing():
    def process(file, min_, height):
        dataloader = PPK_Processing_Result_DataLoader(file_name=file, minutes_limit=min_, height_limit=height)
        PPK_file = dataloader.save_files(app.config['RESULT_DIR'])
        return PPK_file
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['PPK_Processing']:
            add_to_history(name='PPK Processing', logged_in=0)
            file = request.files['file']
            minutes = float(request.form['minutes_limit'])
            height = float(request.form['height_limit'])
            if file and minutes and height:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['RESULT_DIR'], filename)
                file.save(file_path)
                # Process the file
                try:
                    PPK_file, empty_file, text_files = process(file_path, minutes, height)
                    text_files = [os.path.basename(filee) for filee in text_files]
                    result_files = [os.path.basename(PPK_file), os.path.basename(empty_file)] + text_files
                    session['files'] = [os.path.basename(PPK_file), os.path.basename(empty_file)] + text_files
                    result_url = url_for('results', files=result_files)
                    return {'result_url': result_url}
                except:
                    add_to_history(name='PPK Processing', logged_in=2)
                    flash('Wrong Inputs')
                    return redirect(url_for('PPK_processing'))
        else:
            add_to_history(name='PPK Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('PPK_processing'))
    return render_template('PPK_process.html')

@app.route('/CSDP_processing', methods=['GET', 'POST'])
def CSDP_processing():
    def process(file1, file2, file3):
        dataloader = CSDP_DataLoader(file1, file2, file3)
        dataloader.fit()
        CSDP_file = dataloader.save_files(app.config['RESULT_DIR'])
        return CSDP_file
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['CSDP_Processing']:
            add_to_history(name='CSDP Processing', logged_in=0)
            file1 = request.files['file1']
            file2 = request.files['file2']
            file3 = request.files['file3']
            if file1 and file2 and file3:
                filename1 = secure_filename(file1.filename)
                file_path1 = os.path.join(app.config['RESULT_DIR'], filename1)
                file1.save(file_path1)
                filename2 = secure_filename(file2.filename)
                file_path2 = os.path.join(app.config['RESULT_DIR'], filename2)
                file2.save(file_path2)
                filename3 = secure_filename(file3.filename)
                file_path3 = os.path.join(app.config['RESULT_DIR'], filename3)
                file3.save(file_path3)
                # Process the file
                try:
                    CSDP_file = process(file_path1, file_path2, file_path3)
                    result_files = [os.path.basename(CSDP_file)]
                    session['files'] = [os.path.basename(CSDP_file)]
                    result_url = url_for('results', files=result_files)
                    return {'result_url': result_url}
                except:
                    add_to_history(name='CSDP Processing', logged_in=2)
                    flash('Wrong Inputs')
                    return redirect(url_for('CSDP_processing'))
        else:
            add_to_history(name='CSDP Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('CSDP_processing'))
    return render_template('CSDP_process.html')

@app.route('/play_movie')
def play_movie():
    movie_directory = app.config['MOVIE_FOLDER']
    movie_file = next((f for f in os.listdir(movie_directory) if f.endswith(('mp4', 'avi', 'mkv', "m4v"))), None)
    if movie_file:
        return render_template('play_movie.html', movie_file=movie_file)
    else:
        flash('No movie file found')
        return redirect(url_for('index'))
    
@app.route('/movie/<filename>')
def movie(filename):
    return send_from_directory(app.config['MOVIE_FOLDER'], filename)

@app.route('/Image_processing', methods=['GET', 'POST'])
def Image_processing():
    if request.method == 'POST':
        password = request.form["password"]
        if password == passwords["Image_Processing"]: 
            add_to_history(name='Image Processing', logged_in=0)
            add_to_history(name='ImageProcessingAPP.rar', logged_in=3)
            return send_from_directory(app.config['APP_FOLDER'], 'ImageProcessingAPP.rar', as_attachment=True)
        else:
            add_to_history(name='Image Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('image_processing'))
    return render_template('image_processing.html')

@app.route('/delete_empty_processing', methods=['GET', 'POST'])
def delete_empty_processing():
    def process(file, left_bound, right_bound):
        dataloader = Delete_Distance_From_Centerline(file, left_bound=left_bound, right_bound=right_bound)
        dataloader.fit()
        csv_file = dataloader.save_files(app.config['RESULT_DIR'])
        return csv_file
    if request.method == 'POST':
        password = request.form['password']
        if password == passwords['Delete_empty_processing']:
            add_to_history(name='Delete Empty Processing', logged_in=0)
            file = request.files['file']
            left = float(request.form['left'])
            right = float(request.form['right'])
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['RESULT_DIR'], filename)
                file.save(file_path)
                # Process the file
                try:
                    csv_file = process(file_path, left, right)
                    result_files = [os.path.basename(csv_file)]
                    session['files'] = [os.path.basename(csv_file)]
                    result_url = url_for('results', files=result_files)
                    return {'result_url': result_url}
                except:
                    add_to_history(name='Delete Empty Processing', logged_in=2)
                    flash('Wrong Inputs')
                    return redirect(url_for('delete_empty_processing'))
        else:
            add_to_history(name='Delete Empty Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('delete_empty_processing'))
    return render_template('delete_empty_process.html')

@app.route('/culvert_processing', methods=['GET', 'POST'])
def culvert_processing():
    if request.method == 'POST':
        password = request.form["password"]
        if password == passwords["culvert_desing"]: 
            add_to_history(name='Culvert Processing', logged_in=0)
            add_to_history(name='CulvertProcessingApp.rar', logged_in=3)
            return send_from_directory(app.config['APP_FOLDER'], 'CulvertProcessingApp.rar', as_attachment=True)
        else:
            add_to_history(name='Culvert Processing', logged_in=1)
            flash('Incorrect password')
            return redirect(url_for('culvert_process'))
    return render_template('culvert_process.html')

assistant_response = context

@app.route('/talk_to_assistant', methods=['GET', 'POST'])
def talk_to_assistant():
    global assistant_response
    if request.method == 'POST':
        user_input = request.form['message']  # Capture the user's input
        # Here you would call your LM Studio model API or local endpoint to get a response
        assistant_response = send_to_assistant_d(user_input)
        return render_template('assistant.html', user_input=user_input, assistant_response=assistant_response)
    return render_template('assistant.html', user_input=None, assistant_response=None)

@app.route('/send_to_assistant_d', methods=['POST'])
def send_to_assistant_d():
    global assistant_response
    # Get the user input from the form data
    user_input = request.form.get('user-input')
    if user_input:
        # Send user input to the assistant function
        assistant_response = send_to_assistant(user_input+"</Question></Prompt>")
        add_to_history(name="User: "+user_input+" === Assistant: "+assistant_response, logged_in=3)
        return jsonify({'response': assistant_response, 'user_message': user_input})
    return jsonify({'response': None, 'user_message': None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
