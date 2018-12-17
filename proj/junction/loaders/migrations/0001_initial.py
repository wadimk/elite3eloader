# Generated by Django 2.1.3 on 2018-12-17 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the attribute (case sensitive)', max_length=64)),
                ('type', models.CharField(choices=[('Child', 'Child'), ('Parent', 'Parent')], default='Child', help_text='Does this belong to the parent object or the child?', max_length=64)),
                ('sort', models.IntegerField(default=1, help_text='Numerical value to control the order of the fields')),
                ('is_key', models.BooleanField(default=False, help_text='Select for a key field')),
                ('alias_field', models.CharField(blank=True, help_text='If provided, will be used as the AliasField', max_length=256, null=True)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('sort', 'name'),
            },
        ),
        migrations.CreateModel(
            name='AvailableAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The field or attribute id from the object', max_length=64)),
                ('alias_field', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_headers', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('process_xml', models.TextField(blank=True, null=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('response', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-submitted'],
            },
        ),
        migrations.CreateModel(
            name='Loader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Common name for this loader', max_length=64, unique=True)),
                ('description', models.TextField(blank=True, help_text="Description of this loader's purpose", null=True)),
                ('active', models.BooleanField(default=True)),
                ('parent_action', models.CharField(choices=[('Add', 'Add'), ('Edit', 'Edit')], default='Edit', help_text='The type of action this loader performs', max_length=64)),
                ('parent_object', models.CharField(help_text='The primary object we are action upon', max_length=256)),
                ('child_action', models.CharField(blank=True, choices=[('Add', 'Add'), ('Edit', 'Edit')], default='Add', help_text='If applicable, the child action to be performed', max_length=64, null=True)),
                ('child_object', models.CharField(blank=True, help_text='If applicable, the child object we are acting upon', max_length=256, null=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('process', models.CharField(help_text='The 3E process which this loader will call', max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoaderXOQL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for this xoql', max_length=64)),
                ('description', models.TextField(blank=True, help_text='A brief description for this loader', null=True)),
                ('xoql', models.TextField(blank=True, help_text='The xoql to populate the data table on Run tab', null=True, verbose_name='XOQL')),
                ('slug', models.SlugField()),
                ('loader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loaders.Loader')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='loader',
            field=models.ForeignKey(help_text='Select a server to push the data', on_delete=django.db.models.deletion.PROTECT, to='loaders.Loader'),
        ),
        migrations.AddField(
            model_name='history',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servers.Server'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='loader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loaders.Loader'),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together={('name', 'loader')},
        ),
    ]
