# Generated by Django 3.2.3 on 2021-08-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50)),
                ('ItemCat', models.CharField(max_length=15)),
                ('ItemDesc', models.TextField()),
                ('ItemPrice', models.IntegerField()),
                ('ItemImage', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
