# Generated by Django 3.2 on 2023-05-06 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='管理员姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '已使用'), (2, '未使用')], default=2, verbose_name='状态')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.admin', verbose_name='管理员')),
            ],
        ),
        migrations.AddField(
            model_name='admin',
            name='depart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.department', verbose_name='部门'),
        ),
    ]
