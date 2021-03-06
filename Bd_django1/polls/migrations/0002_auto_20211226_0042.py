# Generated by Django 3.2.9 on 2021-12-25 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='Производитель')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Экшн-камера',
                'verbose_name_plural': 'Экшн-камеры',
            },
        ),
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='Производитель')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Фотоаппарат',
                'verbose_name_plural': 'Фотоаппараты',
            },
        ),
        migrations.CreateModel(
            name='MaxResolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Максимальное разрешение',
                'verbose_name_plural': 'Максимальные разрешения',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Тип фотоаппарата',
                'verbose_name_plural': 'Типы фотоаппаратов',
            },
        ),
        migrations.CreateModel(
            name='VideoCameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='Производитель')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('price', models.IntegerField(default=0)),
                ('maxResolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.maxresolution', verbose_name='Максимальное разрешение')),
            ],
            options={
                'verbose_name': 'Видеокамера',
                'verbose_name_plural': 'Видеокамеры',
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='cameras',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.type', verbose_name='Тип фотоаппарата'),
        ),
        migrations.AddField(
            model_name='actioncameras',
            name='maxResolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.maxresolution', verbose_name='Максимальное разрешение'),
        ),
    ]
