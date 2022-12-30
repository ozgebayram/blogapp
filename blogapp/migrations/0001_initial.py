# Generated by Django 4.1.4 on 2022-12-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, max_length=100, null=True)),
                ('category_id', models.BigIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
