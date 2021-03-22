# Generated by Django 3.1.7 on 2021-03-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0007_auto_20210303_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_code', models.CharField(max_length=50)),
                ('cust_number', models.CharField(max_length=50)),
                ('name_customer', models.CharField(max_length=50)),
                ('clear_date', models.CharField(max_length=50)),
                ('buisness_year', models.CharField(max_length=50)),
                ('doc_id', models.CharField(max_length=50)),
                ('posting_date', models.CharField(max_length=50)),
                ('document_create_date', models.CharField(max_length=50)),
                ('document_create_date1', models.CharField(max_length=50)),
                ('due_in_date', models.CharField(max_length=50)),
                ('invoice_currency', models.CharField(max_length=50)),
                ('document_type', models.CharField(max_length=50)),
                ('posting_id', models.CharField(max_length=50)),
                ('area_business', models.CharField(max_length=50)),
                ('total_open_amount', models.CharField(max_length=50)),
                ('baseline_create_date', models.CharField(max_length=50)),
                ('cust_payment_terms', models.CharField(max_length=50)),
                ('invoice_id', models.CharField(max_length=50)),
                ('isOpen', models.CharField(max_length=50)),
            ],
        ),
    ]