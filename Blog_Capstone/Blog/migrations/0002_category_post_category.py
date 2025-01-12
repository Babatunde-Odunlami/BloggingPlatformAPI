# Generated by Django 5.1.4 on 2025-01-11 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AUTOMOTIVE', 'automotive'), ('ELECTRONICS', 'electronics'), ('FASHION', 'fashion'), ('HOME', 'home'), ('SPORTS', 'sports'), ('BOOKS', 'books'), ('MUSIC', 'music'), ('TOYS', 'toys'), ('GENERAL', 'general'), ('GAMES', 'games'), ('HEALTH', 'health'), ('LIFESTYLE', 'lifestyle'), ('OTHERS', 'others')], default='OTHERS', max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Blog.category'),
        ),
    ]
