from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

from models import User, Post

def register_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first() is not None:
            return jsonify({'message': 'User already exists'}), 400
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Registered successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user is None or not user.check_password(data['password']):
            return jsonify({'message': 'Invalid credentials'}), 401
        access_token = create_access_token(identity={'username': user.username, 'email': user.email})
        return jsonify(access_token=access_token)

    @app.route('/logout', methods=['POST'])
    @jwt_required()
    def logout():
        return jsonify({'message': 'Logged out successfully'}), 200

    @app.route('/posts', methods=['GET'])
    def get_posts():
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        posts = Post.query.offset(offset).limit(per_page).all()
        total = Post.query.count()
        pagination = Pagination(page=page, per_page=per_page, total=total, record_name='posts')
        return jsonify({
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': pagination.page,
            'next_page': pagination.next_num,
            'prev_page': pagination.prev_num,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'posts': [post.to_dict() for post in posts]
        })

    @app.route('/posts/<int:id>', methods=['GET'])
    def get_post(id):
        post = Post.query.get_or_404(id)
        return jsonify(post.to_dict())

    @app.route('/posts', methods=['POST'])
    @jwt_required()
    def create_post():
        data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        new_post = Post(title=data['title'], content=data['content'], user_id=user.id)
        db.session.add(new_post)
        db.session.commit()
        return jsonify(new_post.to_dict()), 201

    @app.route('/posts/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_post(id):
        post = Post.query.get_or_404(id)
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if post.user_id != user.id:
            return jsonify({'message': 'Permission denied'}), 403
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        db.session.commit()
        return jsonify(post.to_dict())

    @app.route('/posts/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_post(id):
        post = Post.query.get_or_404(id)
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user['username']).first()
        if post.user_id != user.id:
            return jsonify({'message': 'Permission denied'}), 403
        db.session.delete(post)
        db.session.commit()
        return '', 204

register_routes(app)
