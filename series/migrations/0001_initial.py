# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('season', models.PositiveSmallIntegerField(default=1, verbose_name='\u0421\u0435\u0437\u043e\u043d')),
                ('number', models.PositiveSmallIntegerField(default=1, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0435\u0440\u0438\u0438')),
                ('source', models.CharField(default='', max_length=255, verbose_name='\u0412\u0438\u0434\u0435\u043e\u0444\u0430\u0439\u043b')),
                ('preview', models.CharField(default='', max_length=255, verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('is_published', models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0438\u044f',
                'verbose_name_plural': '\u0421\u0435\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(default='', max_length=3000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('original_language', models.CharField(choices=[('en', '\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'), ('ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), ('ch', '\u041a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0439')], default='en', max_length=24, verbose_name='\u042f\u0437\u044b\u043a \u0441\u0435\u0440\u0438\u0430\u043b\u0430')),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0438\u0430\u043b',
                'verbose_name_plural': '\u0421\u0435\u0440\u0438\u0430\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0433',
                'verbose_name_plural': '\u0422\u0435\u0433\u0438',
            },
        ),
        migrations.AddField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='series', to='series.Tag', verbose_name='\u0422\u0435\u0433\u0438'),
        ),
        migrations.AddField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='series.Series', verbose_name='\u0421\u0435\u0440\u0438\u0430\u043b'),
        ),
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='episodes', to='series.Tag', verbose_name='\u0422\u0435\u0433\u0438'),
        ),
    ]
