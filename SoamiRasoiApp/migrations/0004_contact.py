# Generated by Django 3.2.6 on 2021-08-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoamiRasoiApp', '0003_food_itemdesc'),
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
    ]
