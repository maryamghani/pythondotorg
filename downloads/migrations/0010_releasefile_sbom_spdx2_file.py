# Generated by Django 2.2.24 on 2024-01-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0009_releasefile_sigstore_bundle_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasefile',
            name='sbom_spdx2_file',
            field=models.URLField(blank=True, help_text='SPDX-2 SBOM URL', verbose_name='SPDX-2 SBOM URL'),
        ),
    ]