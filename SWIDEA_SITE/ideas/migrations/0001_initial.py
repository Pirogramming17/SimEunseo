# Generated by Django 4.0.6 on 2022-07-20 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('type', models.CharField(max_length=50, verbose_name='종류')),
                ('description', models.TextField(verbose_name='설명')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('image', models.ImageField(blank=True, upload_to='ideas/%y%m%d', verbose_name='이미지')),
                ('description', models.TextField(verbose_name='설명')),
                ('interest', models.IntegerField(verbose_name='관심도')),
                ('tool_choice', models.CharField(max_length=50, null=True, verbose_name='개발툴')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_tool', to='ideas.tool')),
            ],
        ),
    ]
