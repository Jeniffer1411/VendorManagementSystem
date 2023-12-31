# Generated by Django 4.2.6 on 2023-12-21 06:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendorApp', '0004_vendor_average_response_time_vendor_fulfillment_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 21, 6, 48, 7, 332454, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 6, 48, 26, 357835, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorApp.vendor'),
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorApp.vendor')),
            ],
        ),
    ]
