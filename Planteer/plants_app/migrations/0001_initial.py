# Generated by Django 5.1.3 on 2024-11-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('category', models.CharField(choices=[('Flowers', 'Flowers'), ('Trees', 'Trees'), ('Fruits', 'Fruits'), ('Vegetables', 'Vegetables')], default='Trees', max_length=20)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
