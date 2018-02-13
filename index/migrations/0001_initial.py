# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-12 12:46
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u4f5c\u8005\u540d')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='Base_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(max_length=100000, verbose_name='\u5185\u5bb9')),
                ('summary', models.TextField(max_length=10000, verbose_name='\u6458\u8981')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('isPublic', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('isGuide', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe4\xb8\x9a\xe5\x8a\xa1\xe6\x8c\x87\xe5\x8d\x97')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Author')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u6307\u5357\u6587\u7ae0',
                'verbose_name_plural': '\u4e1a\u52a1\u6307\u5357\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Base_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u57fa\u7840\u77e5\u8bc6\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u57fa\u7840\u77e5\u8bc6\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(max_length=100000, verbose_name='\u5185\u5bb9')),
            ],
        ),
        migrations.CreateModel(
            name='Fee_Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u8d39\u7387\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u8d39\u7387\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Friend_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=100, verbose_name='\u53cb\u94fe\u540d')),
                ('link_url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('isShow', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5c55\u793a')),
            ],
            options={
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5\u7ba1\u7406',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Img_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u540d')),
                ('img_url', models.ImageField(upload_to=b'', verbose_name='\u56fe\u7247')),
                ('link', models.URLField(verbose_name='\u5bf9\u5e94\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u6240\u6709\u56fe\u7247',
                'verbose_name_plural': '\u6240\u6709\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Index_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100, verbose_name='\u56fe\u7247\u4f4d\u7f6e')),
                ('img', models.ManyToManyField(to='index.Img_all')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u56fe',
                'verbose_name_plural': '\u9996\u9875\u56fe',
            },
        ),
        migrations.CreateModel(
            name='Introduce_Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u4fe1\u606f\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u4e1a\u52a1\u4fe1\u606f\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Join_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('aim', models.IntegerField(choices=[(1, '\u4e1a\u52a1\u529e\u7406'), (2, '\u6d3b\u52a8\u62a5\u540d'), (3, '\u5176\u4ed6'), (4, '\u8def\u8fc7\uff0c\u60f3\u4e86\u89e3\u4e00\u4e0b')], verbose_name='\u76ee\u7684')),
                ('phone', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('place', models.CharField(max_length=10000, verbose_name='\u5730\u5740')),
                ('others', models.CharField(max_length=50000, verbose_name='\u5176\u4ed6')),
                ('isRead', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8bfb')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u52a0\u5165\u6211\u4eec\u63d0\u4ea4\u5185\u5bb9',
                'verbose_name_plural': '\u52a0\u5165\u6211\u4eec\u63d0\u4ea4\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Page_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(max_length=200000, verbose_name='\u5185\u5bb9')),
                ('position', models.IntegerField(choices=[(0, '\u9996\u9875\u8f6e\u64ad\u56fe\u6587\u5b57'), (1, '\u5173\u4e8e\u6211\u4eec'), (2, '\u52a0\u5165\u6211\u4eec\u4e0a\u65b9\u6587\u5b57'), (3, '\u52a0\u5165\u6211\u4eec\u4e0b\u65b9\u6587\u5b57')], verbose_name='\u6240\u5728\u4f4d\u7f6e')),
            ],
            options={
                'verbose_name': '\u9875\u9762\u5185\u5bb9',
                'verbose_name_plural': '\u9875\u9762\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='Page_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200000, verbose_name='\u5185\u5bb9')),
                ('position', models.IntegerField(choices=[(0, '\u4e2a\u80a1\u671f\u6743\u6587\u5b57'), (1, '\u5bfc\u822a\u53f3\u4e0a\u89d2\u6587\u5b57')], verbose_name='\u6240\u5728\u4f4d\u7f6e')),
            ],
            options={
                'verbose_name': '\u9875\u9762\u5185\u5bb9\uff08\u7eaf\u6587\u5b57\uff09',
                'verbose_name_plural': '\u9875\u9762\u5185\u5bb9\uff08\u7eaf\u6587\u5b57\uff09',
            },
        ),
        migrations.CreateModel(
            name='Search_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(max_length=100000, verbose_name='\u5185\u5bb9')),
                ('summary', models.TextField(max_length=10000, verbose_name='\u6458\u8981')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('isPublic', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('isHighLight', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xba\xe8\xa6\x81\xe9\x97\xbb')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Author')),
            ],
            options={
                'verbose_name': '\u7814\u7a76\u8d44\u8baf\u6587\u7ae0',
                'verbose_name_plural': '\u7814\u7a76\u8d44\u8baf\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Search_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u7814\u7a76\u8d44\u8baf\u5173\u952e\u8bcd',
                'verbose_name_plural': '\u7814\u7a76\u8d44\u8baf\u5173\u952e\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Fee_content',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='index.Content')),
                ('keyword', models.ManyToManyField(to='index.Fee_Keyword')),
            ],
            options={
                'verbose_name': '\u8d39\u7387\u9875\u9762\u5185\u5bb9',
                'verbose_name_plural': '\u8d39\u7387\u9875\u9762\u5185\u5bb9',
            },
            bases=('index.content',),
        ),
        migrations.CreateModel(
            name='Introduce_content',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='index.Content')),
                ('keyword', models.ManyToManyField(to='index.Introduce_Keyword')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u4fe1\u606f\u9875\u9762\u5185\u5bb9',
                'verbose_name_plural': '\u4e1a\u52a1\u4fe1\u606f\u9875\u9762\u5185\u5bb9',
            },
            bases=('index.content',),
        ),
        migrations.AddField(
            model_name='search_article',
            name='keyword',
            field=models.ManyToManyField(to='index.Search_keyword'),
        ),
        migrations.AddField(
            model_name='base_article',
            name='keyword',
            field=models.ManyToManyField(to='index.Base_keyword'),
        ),
    ]