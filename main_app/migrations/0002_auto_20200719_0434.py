# Generated by Django 3.0.8 on 2020-07-19 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentsdetails',
            name='student_name',
            field=models.ForeignKey(db_column='student_name', on_delete=django.db.models.deletion.PROTECT, to='main_app.StudentDetails'),
        ),
    ]
