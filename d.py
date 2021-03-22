import sqlite3
conn = sqlite3.connect("db.sqlite3")
cur=conn.cursor()

sql= """
    CREATE TABLE t1 (
        business_code TEXT,
        cust_number TEXT,
        name_customer TEXT,
        clear_date TEXT,
        buisness_year TEXT,
        doc_id TEXT,
        posting_date TEXT,
        document_create_date TEXT,
        document_create_date1 TEXT,
        due_in_date TEXT,
        invoice_currency TEXT,
        document_type TEXT,
        posting_id TEXT,
        area_business TEXT,
        total_open_amount TEXT,
        baseline_create_date TEXT,
        cust_payment_terms TEXT,
        invoice_id TEXT,
        isOpen TEXT
    )
    """

cur.execute(sql)
print("done")

conn.commit()
conn.close()