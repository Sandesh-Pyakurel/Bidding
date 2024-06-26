# Generated by Django 5.0.6 on 2024-06-15 14:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_auctioner',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('base_price', models.IntegerField()),
                ('program_id', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('ending_date', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('auctioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctioner_set', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BidsToAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(max_length=255)),
                ('bidding_date', models.DateTimeField(auto_now_add=True)),
                ('bid_number', models.PositiveSmallIntegerField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
