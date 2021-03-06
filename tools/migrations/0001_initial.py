# Generated by Django 3.2 on 2021-05-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('serial_number', models.CharField(max_length=140)),
                ('model', models.CharField(max_length=140)),
                ('mainteance_date', models.DateField(blank=True, null=True)),
                ('is_in_maintain', models.BooleanField(default=False)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('has_tracker', models.BooleanField(default=False)),
                ('tracker_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
