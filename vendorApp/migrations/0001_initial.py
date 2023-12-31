# Generated by Django 4.2.6 on 2023-12-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProfileManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100)),
                ('vendor_contact_details', models.TextField()),
                ('vendor_address', models.TextField()),
                ('vendor_code', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
