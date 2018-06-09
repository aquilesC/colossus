# Generated by Django 2.0.6 on 2018-06-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0014_auto_20180608_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='recipients_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campaign',
            name='unique_clicks_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campaign',
            name='unique_opens_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
