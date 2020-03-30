# Generated by Django 3.0.4 on 2020-03-29 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_client_pseudo'),
        ('commande', '0004_auto_20200329_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='membre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='quantite',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
