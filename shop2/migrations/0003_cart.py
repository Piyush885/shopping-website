# Generated by Django 3.2.8 on 2021-11-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0002_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]