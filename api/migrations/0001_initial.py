# Generated by Django 3.2.14 on 2022-08-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Roll_Number', models.IntegerField()),
                ('School_Name', models.CharField(max_length=100)),
            ],
        ),
    ]