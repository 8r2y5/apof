# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ingredients', models.ManyToManyField(blank=True, to='menus.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='Normal size', max_length=50, unique=True)),
                ('value', models.DecimalField(blank=True, decimal_places=0, max_digits=3)),
                ('value_unit', models.CharField(blank=True, max_length=15)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='menus.Ingredient')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Size'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menus.Restaurant'),
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu'),
        ),
        migrations.AlterUniqueTogether(
            name='topping',
            unique_together=set([('menu', 'ingredient')]),
        ),
        migrations.AlterUniqueTogether(
            name='size',
            unique_together=set([('menu', 'value', 'value_unit')]),
        ),
    ]
