# Generated by Django 4.2.3 on 2024-05-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aftosalon',
            name='rasmi',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aftosalon',
            name='yil',
            field=models.IntegerField(),
        ),
    ]
