# Generated by Django 3.0.8 on 2020-07-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('profile_photo', models.ImageField(default='static/images/nophoto.png', upload_to='static/images/profile_pics')),
            ],
        ),
    ]