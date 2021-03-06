# Generated by Django 3.2.5 on 2021-11-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('note', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_due', models.DateTimeField()),
                ('complete', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('category', models.CharField(choices=[('General', 'General'), ('Body Exercise', 'Body Exercise'), ('Learning', 'Learning'), ('Chores', 'Chores')], default='General', max_length=20)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
