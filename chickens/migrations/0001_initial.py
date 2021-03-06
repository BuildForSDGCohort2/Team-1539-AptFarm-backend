# Generated by Django 3.0.8 on 2020-10-04 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('procedures', '0002_animaldiseases_chemical_fertilizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(max_length=50, null=True)),
                ('drugs', models.ManyToManyField(null=True, to='procedures.Drugs')),
                ('feed', models.ManyToManyField(null=True, to='procedures.Feed')),
                ('procedures', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procedures.Procedures')),
                ('vaccine', models.ManyToManyField(null=True, to='procedures.Vaccine')),
            ],
        ),
    ]
