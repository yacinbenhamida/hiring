# Generated by Django 3.1.1 on 2020-10-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('source_id', models.IntegerField()),
                ('source_name', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=512, null=True)),
                ('address', models.CharField(max_length=512)),
                ('postal_code', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=512)),
                ('website', models.CharField(max_length=512)),
                ('country', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('left_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_company', to='companies.companies')),
                ('right_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_company', to='companies.companies')),
            ],
        ),
    ]
