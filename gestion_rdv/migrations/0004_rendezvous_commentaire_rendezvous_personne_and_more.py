# Generated by Django 4.1.7 on 2023-03-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_rdv', '0003_rendezvous_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='commentaire',
            field=models.TextField(max_length=550, null=True),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='personne',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='nom',
            field=models.CharField(max_length=255),
        ),
    ]
