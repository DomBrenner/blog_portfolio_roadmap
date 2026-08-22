from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable = False)
    tags = db.Column(db.Text, nullable = False)
    createdAt = db.Column(db.DateTime, nullable = False)
    updatedAt = db.Column(db.DateTime, nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "tags": self.tags.split(", "),
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }