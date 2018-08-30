# Generated by Django 2.1 on 2018-08-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('britecore', '0002_customdatafield_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='risktypes',
            name='label',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customdatafield',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='risktypes',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]