# Generated by Django 4.0.5 on 2022-06-29 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('sum', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('client_org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.organization')),
            ],
        ),
    ]