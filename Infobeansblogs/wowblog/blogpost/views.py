from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from wowblog import db
from wowblog.models import BlogPost
from wowblog.blogpost.forms import BlogPostForm
from wowblog.blogpost.bimage_handler import add_blog_img


blogpost = Blueprint('blogpost', __name__)


#CREATE

@blogpost.route('/create',  methods=['GET', 'POST'])
@login_required
def create_post():

    form = BlogPostForm()

    if form.validate_on_submit():
        image = form.bimg.data
        if image :
            filename = add_blog_img(form.bimg.data)
        blogpost = BlogPost(title=form.title.data,
                            text = form.text.data,
                            user_id = current_user.id,
                            bimg=filename
                            )
        db.session.add(blogpost)
        db.session.commit()
        flash("Post Created...")
        return redirect(url_for('core.index'))

    return render_template('create_post.html', title="Add", form=form)
        

#LIST
@blogpost.route("/blogs/<int:blog_post_id>")
def blog_post(blog_post_id):
    blogpost = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blogpost.html', title=blogpost.title, date=blogpost.date, post = blogpost)



#UPDATE
@blogpost.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def update_post(blog_post_id):
    blogpost = BlogPost.query.get_or_404(blog_post_id)

    if blogpost.author != current_user:
        abort(403)
    
    form  = BlogPostForm()
    if form.validate_on_submit():
        if form.bimg.data:
            filename = add_blog_img(form.bimg.data)
            blogpost.bimg = filename

        blogpost.title = form.title.data
        blogpost.text = form.text.data                            
        db.session.commit()
        flash("Post Updated...")
        return redirect(url_for('blogpost.blog_post', blog_post_id=blogpost.id))

    elif request.method == 'GET':
        form.title.data = blogpost.title
        form.text.data = blogpost.text
        form.bimg.data = blogpost.bimg
    
    return render_template('create_post.html', title="Update",  form=form)



#DELETE

@blogpost.route('/<int:blog_post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):
    blogpost = BlogPost.query.get_or_404(blog_post_id)
    if blogpost.author != current_user:
        abort(403)
    
    db.session.delete(blogpost)
    db.session.commit()
    flash("Post Deleted Successfully...")
    return redirect(url_for('core.index'))















