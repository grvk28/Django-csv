from django.shortcuts import render,redirect,get_object_or_404
from .forms import m,m1
from .models import Items,t1
#, ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import UpdateView
#from django.urls import reverse
import csv, sqlite3

con = sqlite3.connect(":memory:") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE t (business_code,cust_number,name_customer,clear_date,buisness_year,doc_id,posting_date,document_create_date,document_create_date1,due_in_date,invoice_currency,document_type,posting_id,area_business,total_open_amount,baseline_create_date,cust_payment_terms,invoice_id,isOpen);") # use your column names here

with open('sbs/data.csv','r') as fin: # `with` statement available in 2.5+ sbs/data.csv
    #csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['business_code'],i['cust_number'],i['name_customer'],i['clear_date'],i['buisness_year'],i['doc_id'],i['posting_date'],i['document_create_date'],i['document_create_date'],i['due_in_date'],i['invoice_currency'],i['document_type'],i['posting_id'],i['area_business'],i['total_open_amount'],i['baseline_create_date'],i['cust_payment_terms'],i['invoice_id'],i['isOpen']) for i in dr]

cur.executemany("INSERT INTO t (business_code,cust_number,name_customer,clear_date,buisness_year,doc_id,posting_date,document_create_date,document_create_date1,due_in_date,invoice_currency,document_type,posting_id,area_business,total_open_amount,baseline_create_date,cust_payment_terms,invoice_id,isOpen) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()





# Create your views here.
@login_required
def index(request):
    user=request.user
    myitems=Items.objects.filter(user=user)
    context={
        'It': myitems
        #"Quantity":myitems.Quantity
        #'status': myitems.status
    }
    return render(request,"index.html",context)

def index1(request):
    return render(request,"index.html")

@login_required
def add(request):
    user=request.user
    list1 = m() 
    if request.method =="POST":
        form = m(request.POST) 
        if form.is_valid():
            Item=form.cleaned_data.get('Item')
            Quantity=form.cleaned_data.get('Quantity')
            status=form.cleaned_data.get('status')
            date=form.cleaned_data.get('date')
            Items.objects.create(user=user,Item=Item, Quantity=Quantity,slug=user.username, status=status,date=date)
            #obj = views.objects.get('index')
            return redirect(index)
      
    return render(request,"add.html",{'form':list1})


class update(UpdateView):
    model=Items
    form_class=m1
    template_name='update.html'
    redirect=index
    

@login_required
def delete(request,id):
    obj=Items.objects.filter(id=id).delete()
    return redirect(index)
            #print(form.errors)
    #return reverse("index")

@login_required  
def filter(request):
    query=request.GET.get('q')
    result=Items.objects.filter(date=query)
    user=request.user
    re=result.filter(user=user)
    context={
        'It':re
    }
    
    return render(request,"index.html",context)

def i(request):
    #user=request.user
    #c = t.objects.count()
    #print(c+2)
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()

    with open('sbs/data.csv','r') as file:
        no_records=0
        for row in file:
            cursor.execute("INSERT INTO t1 (business_code,cust_number,name_customer,clear_date,buisness_year,doc_id,posting_date,document_create_date,document_create_date1,due_in_date,invoice_currency,document_type,posting_id,area_business,total_open_amount,baseline_create_date,cust_payment_terms,invoice_id,isOpen) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", row.split(","))
            connection.commit()
            no_records+=1
        connection.close()
        print('\n{} Records Transferred', format(no_records))
    c1 = t1.objects.count()
    print(c1+2)
    myitems=t1.objects.all()
    context={
        'It': myitems
        #"Quantity":myitems.Quantity
        #'status': myitems.status
    }
    return render(request,"home.html",context)
