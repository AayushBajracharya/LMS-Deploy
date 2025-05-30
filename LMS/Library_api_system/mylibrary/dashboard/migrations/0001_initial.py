# Generated by Django 5.1.6 on 2025-02-16 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverdueBorrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_id', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_student_count', models.IntegerField(default=0)),
                ('total_book_count', models.IntegerField(default=0)),
                ('total_transaction_count', models.IntegerField(default=0)),
                ('total_borrowed_books', models.IntegerField(default=0)),
                ('total_returned_books', models.IntegerField(default=0)),
                ('overdue_borrowers', models.ManyToManyField(related_name='dashboards', to='dashboard.overdueborrower')),
            ],
        ),
    ]
