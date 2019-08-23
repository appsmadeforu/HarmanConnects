# Generated by Django 2.1 on 2019-08-23 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialize.Employee')),
            ],
        ),
    ]
