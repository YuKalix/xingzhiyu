# Generated by Django 2.1 on 2019-06-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='success_case/%Y/%m', verbose_name='展示图')),
                ('describe', models.CharField(default='', max_length=50, verbose_name='案列简介')),
                ('url', models.URLField(verbose_name='案例链接')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否展示')),
            ],
            options={
                'verbose_name': '案例',
                'verbose_name_plural': '案例',
            },
        ),
    ]
