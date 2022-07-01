# Generated by Django 4.0.5 on 2022-07-01 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='client_org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.organization'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='client_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.client'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]