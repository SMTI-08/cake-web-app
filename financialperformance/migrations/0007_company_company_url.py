# Generated by Django 2.1.4 on 2019-01-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financialperformance', '0006_company_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
