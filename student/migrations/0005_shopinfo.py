# Generated by Django 2.2.2 on 2019-06-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_upazilainfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=80)),
                ('Rent', models.IntegerField()),
                ('PaidRent', models.IntegerField()),
                ('comments', models.CharField(max_length=50)),
            ],
        ),
    ]
