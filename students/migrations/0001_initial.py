# Generated by Django 5.1.7 on 2025-03-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('course', models.CharField(choices=[('Full Stack Web Development with Python and Django', 'Full Stack Web Development with Python and Django'), ('Machine Learning', 'Machine Learning'), ('Data Science', 'Data Science'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Cyber Security', 'Cyber Security')], max_length=50)),
            ],
        ),
    ]
