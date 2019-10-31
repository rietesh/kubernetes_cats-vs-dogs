import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
import use_model

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            final_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            ans = use_model.overall(final_path)
            os.remove(final_path)
            return render_template("answer.html" , filepath=ans)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file"/>
      <input type="submit" value="Upload"/>
    </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host="0.0.0.0",debug=True)

    #sess.init_app(app)
    #app.run(debug=True)
