
from wowblog.models import BlogPost,User
from wowblog.models import Carousel
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():

    page = request.args.get('page', 1, type=int)
    blogpost = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    carousel_items = Carousel.query.all()
    return render_template("index.html", blogpost = blogpost,carousel_items=carousel_items)


@core.route('/info')
def info():
    all_users = User.query.all()
    return render_template('info.html', users=all_users)