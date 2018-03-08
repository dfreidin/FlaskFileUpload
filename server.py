from flask import Flask, render_template, request, redirect, flash
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "swordfish"
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/result", methods=["POST"])
def upload():
    file = request.files["file"]
    if file and file.filename != "" and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        msg="Your file has been successfully uploaded"
        cat="good"
        return render_template("result.html", message=msg, category=cat)
    else:
        msg="Your file upload failed. Please Try Again."
        cat="error"
        return render_template("result.html", message=msg, category=cat)
app.run(debug=True)