# Generated by Django 3.2 on 2021-06-09 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0006_auto_20210608_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='application_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
