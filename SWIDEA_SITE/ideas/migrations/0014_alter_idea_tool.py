# Generated by Django 4.0.6 on 2022-07-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0013_idea_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tool',
            field=models.CharField(max_length=50, null=True, verbose_name='개발툴'),
        ),
    ]
