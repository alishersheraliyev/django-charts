# Generated by Django 4.0.4 on 2022-05-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
        migrations.AddField(
            model_name='post',
            name='daromadi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]