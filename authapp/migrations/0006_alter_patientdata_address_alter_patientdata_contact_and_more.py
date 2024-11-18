# Generated by Django 4.2.4 on 2024-07-23 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_patientdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='appointmentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.patientdata')),
            ],
        ),
    ]