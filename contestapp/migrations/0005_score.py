# Generated by Django 5.0 on 2023-12-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestapp', '0004_alter_time_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('question1', models.IntegerField(default=0)),
                ('question2', models.IntegerField(default=0)),
                ('question3', models.IntegerField(default=0)),
                ('question4', models.IntegerField(default=0)),
                ('question5', models.IntegerField(default=0)),
                ('question6', models.IntegerField(default=0)),
                ('question7', models.IntegerField(default=0)),
                ('question8', models.IntegerField(default=0)),
                ('question9', models.IntegerField(default=0)),
                ('question10', models.IntegerField(default=0)),
                ('question11', models.IntegerField(default=0)),
                ('question12', models.IntegerField(default=0)),
                ('question13', models.IntegerField(default=0)),
                ('question14', models.IntegerField(default=0)),
                ('question15', models.IntegerField(default=0)),
                ('question16', models.IntegerField(default=0)),
                ('question17', models.IntegerField(default=0)),
                ('question18', models.IntegerField(default=0)),
                ('question19', models.IntegerField(default=0)),
                ('question20', models.IntegerField(default=0)),
                ('question21', models.IntegerField(default=0)),
                ('question22', models.IntegerField(default=0)),
                ('question23', models.IntegerField(default=0)),
                ('question24', models.IntegerField(default=0)),
                ('question25', models.IntegerField(default=0)),
                ('question26', models.IntegerField(default=0)),
                ('question27', models.IntegerField(default=0)),
                ('question28', models.IntegerField(default=0)),
                ('question29', models.IntegerField(default=0)),
                ('question30', models.IntegerField(default=0)),
                ('score', models.CharField(max_length=100)),
            ],
        ),
    ]
