# Generated by Django 3.1.1 on 2020-09-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(default='SA', max_length=32, null=True),
        ),
    ]
