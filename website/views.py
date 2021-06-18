from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Blog
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user, page='home')

@views.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        if len(title) < 1:
            flash('title is too short', category='error')
        elif len(body) < 1:
            flash('body is too short', category='error')
        else:
            new_blog = Blog(title=title, body=body, user_id=current_user.id)
            db.session.add(new_blog)
            db.session.commit()
            flash('blog added', category='success')

    return render_template("blog.html", user=current_user, page='blog')

@views.route('/delete-blog', methods=['POST'])
def delete_blog():
    blog = json.loads(request.data)
    blogId = blog['blogId']
    blog = Blog.query.get(blogId)
    
    if blog:
        if blog.user_id == current_user.id:
            db.session.delete(blog)
            db.session.commit()
    
    return jsonify({})