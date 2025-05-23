# Generated by Django 5.1.7 on 2025-03-24 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('currently_active', models.BooleanField(default=True)),
                ('role', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.foodcategory')),
            ],
        ),
        migrations.CreateModel(
            name='MOHArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.district')),
            ],
        ),
        migrations.CreateModel(
            name='FoodParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uncertanty', models.CharField(max_length=50, null=True)),
                ('regulatory_limit', models.CharField(max_length=50, null=True)),
                ('is_accredited', models.BooleanField(default=False)),
                ('test_method', models.CharField(max_length=50, null=True)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.foodtype')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='PHIArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('PHIName', models.CharField(max_length=50, null=True)),
                ('moharea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.moharea')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sampleid', models.CharField(max_length=12, unique=True)),
                ('date_collected', models.DateField()),
                ('MOHArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.moharea')),
                ('PHIArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.phiarea')),
                ('foodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.foodtype')),
                ('analysis_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.staffmember')),
            ],
        ),
    ]
