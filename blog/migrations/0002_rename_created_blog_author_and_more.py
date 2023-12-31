# Generated by Django 4.2.2 on 2023-06-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='publish_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published')], default='p', max_length=1),
        ),
    ]
