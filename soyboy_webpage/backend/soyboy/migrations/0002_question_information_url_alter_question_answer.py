# Generated by Django 4.1.7 on 2023-04-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soyboy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='information_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('choice_a', 'A'), ('choice_b', 'B'), ('choice_c', 'C'), ('choice_d', 'D')], default='choice_a', max_length=8),
        ),
    ]