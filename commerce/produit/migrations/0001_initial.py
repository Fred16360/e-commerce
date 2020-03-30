# Generated by Django 3.0.4 on 2020-03-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=20, unique=True)),
                ('categorie', models.CharField(max_length=20)),
                ('titre', models.CharField(max_length=100)),
                ('descritpion', models.TextField()),
                ('couleur', models.CharField(max_length=20)),
                ('taille', models.CharField(max_length=5)),
                ('public', models.CharField(choices=[('M', 'Homme'), ('F', 'Femme'), ('Mixte', 'Mixte')], max_length=5)),
                ('photo', models.ImageField(default='', upload_to='images')),
                ('prix', models.PositiveIntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
