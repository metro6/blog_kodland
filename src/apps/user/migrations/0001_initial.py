# Generated by Django 3.0.5 on 2020-04-06 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='E-mail')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Телефон')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Права на доступ в админ. панель')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Права суперпользователя')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('active', models.BooleanField(default=False, verbose_name='Активный пользователь?')),
                ('activation_hash', models.CharField(blank=True, max_length=40, verbose_name='Хеш пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=32, unique=True, verbose_name='Хеш')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Хеш пользователя',
                'verbose_name_plural': 'Хеши пользователей',
            },
        ),
    ]
