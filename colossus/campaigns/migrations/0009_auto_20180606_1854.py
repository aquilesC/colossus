# Generated by Django 2.0.6 on 2018-06-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0008_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'link', 'verbose_name_plural': 'links'},
        ),
        migrations.AddField(
            model_name='link',
            name='click_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]