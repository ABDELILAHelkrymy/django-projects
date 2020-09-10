# Generated by Django 3.1 on 2020-09-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of message.', max_length=120, null=1)),
                ('message', models.TextField(help_text="what's on your mind ...")),
            ],
        ),
    ]