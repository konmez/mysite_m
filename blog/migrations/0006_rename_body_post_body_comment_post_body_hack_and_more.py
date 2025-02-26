# Generated by Django 5.1.6 on 2025-02-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_trigram_ext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='body_comment',
        ),
        migrations.AddField(
            model_name='post',
            name='body_hack',
            field=models.TextField(default='No hack'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DIY', 'DIY'), ('K', 'Kitchen'), ('H', 'Household'), ('O', 'Other')], default='DIY', max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='effectiveness',
            field=models.CharField(choices=[('GD', 'Good'), ('OK', 'May be'), ('IDK', 'Idk'), ('NG', 'Not good'), ('DN', 'Dangerous')], default='IDK', max_length=3),
        ),
    ]
