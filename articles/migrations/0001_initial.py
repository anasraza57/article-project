# Generated by Django 4.0.5 on 2022-06-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('name_en', models.CharField(max_length=512, null=True)),
                ('name_de', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('created_en', models.DateField(auto_now_add=True, null=True)),
                ('created_de', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('updated_en', models.DateField(auto_now=True, null=True)),
                ('updated_de', models.DateField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=512)),
                ('title_en', models.CharField(max_length=512, null=True)),
                ('title_de', models.CharField(max_length=512, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('thumbnail', models.CharField(blank=True, max_length=10000, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('slug_en', models.SlugField(max_length=100, null=True, unique=True)),
                ('slug_de', models.SlugField(max_length=100, null=True, unique=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_de', models.TextField(null=True)),
                ('tags', models.ManyToManyField(to='articles.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
