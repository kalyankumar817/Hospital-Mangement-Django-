# Generated by Django 4.2.4 on 2024-07-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_signupdata_delete_cusdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]