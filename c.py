import sqlite3, csv

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