# Generated by Django 2.2.6 on 2019-10-24 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0003_assignmentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentmodel',
            name='parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignmentmodel',
            name='assignment',
            field=models.ForeignKey(blank=True, limit_choices_to={'parent': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='CompanyApp.AssignmentModel'),
        ),
    ]
