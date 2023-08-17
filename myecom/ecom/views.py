from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ecom.models import BlogModel
from . import forms,models
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                  CreateView, DeleteView, UpdateView)

from django.urls import reverse_lazy


#forlogin
from django.contrib.auth import authenticate, login , logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    products = models.Product.objects.all()

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    return render(request, 'index.html', {'products': products, 'product_count_in_cart': product_count_in_cart})

#  Registeration method
def register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_user_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and  profile_user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_user_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            register = True        
        else:
            print(user_form.errors, profile_user_form.errors)
    else:
        user_form          =  UserForm()
        profile_user_form  =  UserProfileInfoForm()
    return render(request, 'register.html', context={'user_form':user_form, 'profile_user_form': profile_user_form, 'register':register})


# login method
def user_login(request):

    errorss = ""
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password )

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                errorss = "Account is not active..."
        else:
            print("Someone try to login and failed...")
            print("Username {} and Password {} ".format(username, password) )
            errorss = "Invalid username or password"
    
    return render(request, 'login.html', context={'errors':errorss})


#  logout method
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# public blog method
def blogs(request):
    all_blog_data = BlogModel.objects.all()
    return render(request, 'blogs.html', context={'all_data':all_blog_data})



# CBV based section----------
# Create a new blog method
class BlogCreateView(CreateView):
    fields = ('desc', 'blog_img')
    model = BlogModel

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userid = request.user 
            obj.save()

        return redirect('ecom:my_blog')

    
# Update Blog Method
class BlogUpdateView(UpdateView):
    fields = ('desc', 'blog_img')
    model = models.BlogModel


# List all the blog method
class BlogListView(ListView):
    context_object_name = 'blogmodel_list'
    template_name = 'blogmodel_list.html'

    def get_queryset(self, *args, **kwargs):
       return BlogModel.objects.filter(userid = self.request.user.id)


# view one blog in details method.
class BlogDetailView(DetailView):
    context_object_name = 'blog_details'
    model = models.BlogModel
    template_name = 'ecom/blogmodel_details.html'


# to delete blog
class BlogDeleteView(DeleteView):    
    model = models.BlogModel
    success_url = reverse_lazy('ecom:my_blog')
    template_name = 'ecom/blog_confirm_delete.html'

#any one can add product to cart, no need of signin
def add_to_cart_view(request,pk):
    products=models.Product.objects.all()

    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))+1
    else:
        product_count_in_cart=1

    product = models.Product.objects.get(id=pk)
    messages.success(request, product.name + " added to cart successfully!")
    response = render(request, 'index.html',{'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)


    #messages.info(request, product.name + ' added to cart successfully!')

    return  response



def cart_view(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})


def remove_from_cart_view(request,pk):
    # removing product id from cookie
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Product.objects.all().filter(id__in = product_id_in_cart)
        #for total price shown in cart after removing product
        for p in products:
            total=total+p.price

        #  for update coookie value after removing product id in cart
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]

            # for counter in cart
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter = product_ids.split('|')
            product_count_in_cart = len(set(counter))-1
        else:
            product_count_in_cart = 0

        product = models.Product.objects.get(id=pk)
        messages.error(request, product.name + " removed from cart successfully")
        response = render(request, 'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        product = models.Product.objects.get(id=pk)
        #messages.info(request, product.name + ' removed from cart successfully!')
        return response



def customer_address_view(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    product_in_cart=False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart=True
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            #for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total=0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart=product_ids.split('|')
                    products=models.Product.objects.all().filter(id__in = product_id_in_cart)
                    for p in products:
                        total=total+p.price

            response = render(request, 'payment.html',{'total':total})
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            return response

    return render(request,'customer_address.html',{'addressForm':addressForm,'product_in_cart':product_in_cart,'product_count_in_cart':product_count_in_cart})


def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch customer  mobile, address, Email
    # we will fetch product id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    User = get_user_model()
    Customer = User.objects.get(id=request.user.id)
    #customer=models.User.objects.get(User=request.user.id)
    products=None
    email=None
    mobile=None
    address=None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email=request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile=request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address=request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for product in products:
        models.Orders.objects.get_or_create(userid=Customer,product=product,status='Pending',email=email,mobile=mobile,address=address)

    # after order placed cookies should be deleted
    response = render(request,'payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response


@login_required(login_url='ecom:user_login')
def my_order_view(request):
    User = get_user_model()
    customer = User.objects.get(id=request.user.id)
    orders = models.Orders.objects.all().filter(userid=customer)
    ordered_products = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_products.append(ordered_product)

    return render(request, 'my_order.html', {'data': zip(ordered_products, orders)})

import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

@login_required(login_url='ecom:user_login')
def download_invoice_view(request,orderID,productID):
    order=models.Orders.objects.get(id=orderID)
    product=models.Product.objects.get(id=productID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':product.name,
        'productImage':product.product_image.url,
        'productPrice':product.price,
        'productDescription':product.description,


    }
    return render_to_pdf('download_invoice.html',mydict)

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=models.Product.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    return render(request,'allproducts.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})



def all_product_view(request):
    products = models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    # word variable will be shown in html when user click on search button

    return render(request, 'allproducts.html',
                  {'products': products, 'product_count_in_cart': product_count_in_cart})