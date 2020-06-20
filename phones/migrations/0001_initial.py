# Generated by Django 3.0.7 on 2020-06-19 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_model', models.TextField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('os', models.TextField(choices=[('IOS', 'IOS'), ('Android', 'Android')], max_length=10)),
                ('ram', models.DecimalField(decimal_places=0, max_digits=3)),
                ('pixel_per_inch', models.DecimalField(decimal_places=0, max_digits=6)),
                ('dual_camera', models.BooleanField(choices=[(True, 'Есть'), (False, '-')], default=False)),
                ('cpu', models.TextField(max_length=50)),
                ('screen_resolution', models.TextField(max_length=30)),
                ('fm_radio', models.BooleanField(choices=[(True, 'Есть'), (False, '-')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneAddInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_info', models.TextField(max_length=50)),
                ('phone_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
    ]