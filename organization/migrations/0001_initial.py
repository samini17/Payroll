# Generated by Django 3.2 on 2023-09-05 11:51

from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('avg', models.FloatField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('location', models.CharField(max_length=40, verbose_name='location')),
                ('address', models.TextField(blank=True, verbose_name='address')),
                ('established_date', models.DateField(verbose_name='established date')),
                ('avatar', models.ImageField(blank=True, upload_to='department_avatars/', verbose_name='avatar')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(max_length=40, verbose_name='last name')),
                ('national_code', models.CharField(help_text='It must contain 10 digits...', max_length=10, unique=True, validators=[utils.validators.NationalCodeValidator()], verbose_name='national code')),
                ('phone_number', models.CharField(help_text='It must be a VALID 12 digits like 98xxxxxxxxxx', max_length=11, unique=True, validators=[utils.validators.PhoneNumberValidator()], verbose_name='phone number')),
                ('age', models.PositiveSmallIntegerField(verbose_name='age')),
                ('job_title', models.PositiveSmallIntegerField(choices=[(4, 'help desk'), (5, 'software developer'), (6, 'financial'), (7, 'operator')], default=4, verbose_name='job title')),
                ('marital_status', models.PositiveSmallIntegerField(choices=[(1, 'single'), (2, 'married'), (3, 'divorced')], default=1, verbose_name='marital status')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('degree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.degree', verbose_name='degree')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='SalaryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='from date')),
                ('till_date', models.DateField(verbose_name='till date')),
                ('work_time', models.PositiveSmallIntegerField(default=0, verbose_name='work time')),
                ('hourly_wage_base', models.PositiveIntegerField(default=2000000, verbose_name='hourly wage base')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
            },
        ),
    ]
