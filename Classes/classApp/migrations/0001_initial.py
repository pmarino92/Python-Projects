# Generated by Django 3.2.6 on 2021-08-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('duration', models.DecimalField(decimal_places=3, default=0.0, max_digits=10000)),
            ],
        ),
    ]