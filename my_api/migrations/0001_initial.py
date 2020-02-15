# Generated by Django 3.0.3 on 2020-02-11 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, verbose_name='标题')),
                ('article_content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('article_views', models.IntegerField(default=0, verbose_name='浏览数')),
                ('comment_content', models.IntegerField(default=0, verbose_name='评论总数')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_num', models.IntegerField(default=0, verbose_name='排序')),
                ('category_name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('category_alias', models.CharField(blank=True, max_length=20, null=True, verbose_name='分类别名')),
                ('category_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='分类描述')),
                ('parent_category_id', models.IntegerField(default=-1, verbose_name='父分类id')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, verbose_name='标签名称')),
                ('tag_alias', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签别名')),
                ('tag_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='标签描述')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('user_email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(verbose_name='留言内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_api.Article', verbose_name='所属文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_api.User', verbose_name='留言用户')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='my_api.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='my_api.Tag', verbose_name='文章标签'),
        ),
    ]