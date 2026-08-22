from flask import Flask, request, jsonify
from models import db, Post
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello():
    return("Hello")

@app.route('/posts', methods=['POST'])
def write_article():
    current_time = datetime.now()
    data = request.get_json()
    if request.method == 'POST':
            if "title" not in data or "content" not in data or "category" not in data or "tags" not in data:
                return {"error": "Bad Request."}, 400
            else:
                new_post = Post(title=data["title"], content=data["content"], category=data["category"], tags=data["tags"], createdAt=current_time, updatedAt=current_time)

                db.create_all()
                db.session.add(new_post)
                db.session.commit()
                return new_post.to_dict(), 201

@app.route('/posts', methods = ['GET'])
def get_articles():
    searchstring = request.args.get('term')
    if searchstring:
        posts = Post.query.filter(db.or_(
            Post.title.ilike(f"%{searchstring}%"),
            Post.content.ilike(f"%{searchstring}%"),
            Post.category.ilike(f"%{searchstring}%")
        )).all()
    else:
        posts = Post.query.all()

    return jsonify([p.to_dict() for p in posts])    

@app.route('/posts/<id>', methods = ['GET'])
def get_article(id):
    post = Post.query.get(id)
    if post is None:
        return {"error": "Post not found."}, 404
    return post.to_dict(), 200



@app.route('/posts/<id>', methods = ['PUT'])
def update_post(id):
    current_time = datetime.now()
    post = Post.query.get(id)
    if post is None:
        return {"error": "Post not found."}, 404
    data = request.get_json()
    if request.method == 'PUT':
            if "title" not in data or "content" not in data or "category" not in data or "tags" not in data:
                return {"error": "Bad Request."}, 400
            else:
                post.title = data["title"]
                post.content = data["content"]
                post.category = data["category"]
                post.tags = data["tags"]
                post.updatedAt = current_time
                db.session.add(post)
                db.session.commit()
                return post.to_dict(), 200

@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    if post is None:
        return {"error": "Post not found."}, 404
    db.session.delete(post)
    db.session.commit()
    return '', 204