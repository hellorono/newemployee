# Generated by Django 4.1.7 on 2023-03-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empweb', '0003_employeemaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentmaster',
            name='created_at_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
