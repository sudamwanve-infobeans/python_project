import os
from flask import render_template, url_for, flash, redirect, request, Blueprint,session
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from wowblog import app,db
from wowblog.models import AdminUser,Carousel
from wowblog.admin.forms import AdminRegistrationForm, AdminLoginForm,CarouselForm
from wowblog.admin.image_handler import add_carousel_img


ALLOWED_EXTENSIONS = {'jpg', 'jpeg','avif'}
admin = Blueprint('admin', __name__)



@admin.route('/admin/register', methods=['GET', 'POST'])
def adminReg():
    form = AdminRegistrationForm()

    if form.validate_on_submit():
        adminuser = AdminUser(username=form.username.data,
                    password=form.password.data)

        db.session.add(adminuser)
        db.session.commit()
        flash('Admin registered successfully!', 'success')
        return redirect(url_for('admin.adminLogin'))

    return render_template('admin/register.html', form=form)

@admin.route('/admin/login', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        adminuser = AdminUser.query.filter_by(username=form.username.data).first()

        if adminuser:
            if adminuser.check_password(form.password.data) and adminuser is not None:
                login_user(adminuser)
                flash("Login successful")
                return redirect(url_for('admin.dashboard'))
            else:
                flash("Invalid password")
        else:
            flash("Invalid username")

    return render_template('admin/login.html', form=form)

@admin.route('/admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')


@admin.route('/admin/logout')
def adminLogout():
    logout_user()
    current_user = None
    session.clear()
    flash("You are logged out!")
    return redirect(url_for('admin.adminLogin'))

@admin.route('/admin/carousel', methods=['GET', 'POST'])
def createCarousel():
    form = CarouselForm()

    if form.validate_on_submit():
        image = form.cimg.data
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            filename = add_carousel_img(form.cimg.data)
          #image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_item = Carousel(title=form.title.data,desc=form.desc.data, cimg=filename)
            db.session.add(new_item)
            db.session.commit()
            flash('Carousel item created successfully', 'success')
            return redirect(url_for('admin.listCarousel'))
        else:
            flash('Invalid image format', 'danger')

    return render_template('admin/carousel_create.html', form=form)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@admin.route('/admin/carousel/list')
def listCarousel():
    carousel_items = Carousel.query.all()
    return render_template('admin/carousel_list.html', carousel_items=carousel_items)


@admin.route('/carousel/delete/<int:item_id>', methods=['POST'])
def deleteCarousel(item_id):
    item = Carousel.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin.listCarousel'))