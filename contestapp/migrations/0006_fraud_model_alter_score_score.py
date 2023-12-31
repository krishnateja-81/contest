# Generated by Django 5.0 on 2023-12-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestapp', '0005_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='fraud_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fraud', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
