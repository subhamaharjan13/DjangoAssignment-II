# Generated by Django 3.0.8 on 2020-07-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='static/images/nophoto.png', upload_to='static/images/profile_pics')),
            ],
        ),
    ]