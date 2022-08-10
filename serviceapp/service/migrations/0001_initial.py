# Generated by Django 4.0.5 on 2022-06-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('type_service', models.CharField(max_length=150)),
                ('numero', models.IntegerField(default=False)),
                ('tarifs', models.FloatField(default=0)),
            ],
        ),
    ]
