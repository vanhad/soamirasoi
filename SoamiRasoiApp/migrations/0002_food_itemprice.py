# Generated by Django 3.2.6 on 2021-08-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoamiRasoiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ItemPrice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
