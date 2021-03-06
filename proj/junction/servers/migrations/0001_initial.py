# Generated by Django 2.1.3 on 2018-12-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Common name for the server', max_length=256, unique=True)),
                ('protocol', models.CharField(choices=[('http', 'http'), ('https', 'https')], default='http', help_text='The protocol in use for this server', max_length=64)),
                ('wapi', models.CharField(help_text='The wapi or load balancer to use', max_length=64, verbose_name='WAPI')),
                ('instance', models.CharField(help_text="DB Instance 'TE_3E_UAT' as example", max_length=64)),
                ('custom_wsdl', models.CharField(blank=True, help_text='Full path to the wsdl if not in the typical location', max_length=512, null=True, verbose_name='Custom WSDL')),
                ('active', models.BooleanField(default=True, help_text='Uncheck to remove this server from active listing')),
                ('domain', models.CharField(blank=True, help_text='Optional. If set will override current user credentials (must be set with user/pass fields', max_length=255, null=True, verbose_name='User Domain')),
                ('username', models.CharField(blank=True, help_text='Optional. If set will override current user credentials (must be set with domain/pass fields', max_length=255, null=True, verbose_name='User Name')),
                ('password', models.CharField(blank=True, help_text='Optional. If set will override current user credentials (must be set with domain/user fields', max_length=255, null=True, verbose_name='User Password')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
