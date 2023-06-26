from flask import Flask, render_template, request
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from model import db, User, Entry, Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/upload-tools' , methods=['GET'])
def upload_tools():
    # Retrieve tools with publish=True from the database
    tools = Entry.query.filter_by(publish=True).all()
    tool_data = []
    for tool in tools:
        tool_data.append({
            'description': tool.description,
            'category': tool.category,
            'author': tool.author,
            'tool_url': tool.tool_url,
            'tool_name': tool.tool_name,
            'filename': tool.filename,
            'created_at': tool.created_at
        })
    print('tools=================:', tool_data)
    return render_template('upload.html', tools=tool_data)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Query the database to find a user with the provided username and password
        user = User.query.filter_by(name=username, password=password).first()
        if user:
            # Authentication successful, redirect to index page
            # return render_template('dashboard.html')
            print('login successful')
        else:
            # Authentication failed, show an error message
            error_message = 'Invalid username or password.'
            return render_template('login.html', error=error_message)

    # If it's a GET request, simply render the login page
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user object and add it to the session
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return 'Registration successful'

    return render_template('register.html')


@app.route('/totally-free', methods=['POST', 'GET'])
def totally_free():
    if request.method == 'POST':
        # Retrieve form data
        description = request.form['description']
        category = request.form['category']
        author = request.form['author']
        tool_url = request.form['tool_url']
        tool_name = request.form['tool_name']
        type = 'totally_free'
        publish = False

        # Check if a file was uploaded
        if 'logo' in request.files:
            logo = request.files['logo']

            # Save the uploaded file to the UPLOAD_FOLDER directory
            filename = secure_filename(logo.filename)
            logo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        # Create a new entry in the database
        new_entry = Entry(
            description=description,
            category=category,
            author=author,
            type=type,
            tool_url=tool_url,
            tool_name=tool_name,
            filename=filename,
            created_at=datetime.now(),
            publish=publish
        )

        # Add the entry to the session and commit the changes
        db.session.add(new_entry)
        db.session.commit()

        # Redirect back to the appropriate page
        return "Successfully uploaded your Tool"

    return render_template("totally-free.html")


@app.route('/free-to-try', methods=['POST', 'GET'])
def free_to_try():
    if request.method == 'POST':
        # Retrieve form data
        description = request.form['description']
        category = request.form['category']
        author = request.form['author']
        tool_url = request.form['tool_url']
        tool_name = request.form['tool_name']
        type = 'free_to_try'
        publish = False

        # Check if a file was uploaded
        if 'logo' in request.files:
            logo = request.files['logo']

            # Save the uploaded file to the UPLOAD_FOLDER directory
            filename = secure_filename(logo.filename)
            logo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        # Create a new entry in the database
        new_entry = Entry(
            description=description,
            category=category,
            author=author,
            type=type,
            tool_url=tool_url,
            tool_name=tool_name,
            filename=filename,
            created_at=datetime.now(),
            publish=publish,
        )

        # Add the entry to the session and commit the changes
        db.session.add(new_entry)
        db.session.commit()

        # Redirect back to the appropriate page
        return "Successfully uploaded your free_to_try Tool"

    return render_template("free-to-try.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return 'Message sent'

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
