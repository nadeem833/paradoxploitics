from datbase import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(500))

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))
    category = db.Column(db.String(50))
    author = db.Column(db.String(50))
    type = db.Column(db.String(50))
    tool_url = db.Column(db.String(200))
    tool_name = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    publish = db.Column(db.Boolean, default=False)  # Add new column 'publish' with default value False


    def __init__(self, description, category, author, tool_url, tool_name, filename, created_at, type , publish=False):
        self.description = description
        self.category = category
        self.author = author
        self.type = type
        self.tool_url = tool_url
        self.tool_name = tool_name
        self.filename = filename
        self.created_at = created_at
        self.publish = publish
