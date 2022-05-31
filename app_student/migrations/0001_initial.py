# Generated by Django 4.0.4 on 2022-05-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='заголовок', help_text='<small class="text-muted">это наш заголовок</small><hr><br>', max_length=254, null=True, verbose_name='Заголовок:')),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]