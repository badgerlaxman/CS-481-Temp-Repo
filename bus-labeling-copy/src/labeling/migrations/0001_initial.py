# Generated by Django 3.1 on 2022-12-07 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BIRADSMarginChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'Circumscribed'), ('Not circumscribed', ((1, 'Indistinct'), (2, 'Angular'), (3, 'Microlobulated'), (4, 'Spiculated')))], unique=True, verbose_name='Margin')),
            ],
        ),
        migrations.CreateModel(
            name='Masking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cropping', models.TextField(default='', verbose_name='Cropping')),
                ('tumor', models.TextField(default='', verbose_name='Tumor Mask')),
                ('tissue', models.TextField(default='', verbose_name='Tissue Mask')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BUSDataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Dataset Name')),
                ('path', models.FilePathField(allow_files=False, allow_folders=True, path='/code/media', verbose_name='Dataset Path')),
                ('permission', models.CharField(choices=[('no', 'Private (only the uploader can see)'), ('view', 'Everyone can view'), ('edit', 'Everyone can edit/label'), ('download', 'Everyone can download')], default='no', max_length=20, verbose_name='Permission')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
        migrations.CreateModel(
            name='BIRADS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'Oval'), (1, 'Round'), (2, 'Irregular')], null=True, verbose_name='Shape')),
                ('orientation', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'Parallel'), (1, 'Not Parallel')], null=True, verbose_name='Orientation')),
                ('echo_pattern', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'Anechoic'), (1, 'Hyperechoic'), (2, 'Complex cystic and solid'), (3, 'Hypoechoic'), (4, 'Isoechoic'), (5, 'Heterogeneous')], null=True, verbose_name='Echo Pattern')),
                ('posterior_feature', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'No posterior features'), (1, 'Enhancement'), (2, 'Shadowing'), (3, 'Combined pattern')], null=True, verbose_name='Posterior Features')),
                ('calcification', models.IntegerField(choices=[(-1, 'UNKNOWN'), (0, 'Calcifications in a mass'), (1, 'Calcifications outside of a mass'), (2, 'Intraductal calcifications'), (3, 'NONE')], null=True, verbose_name='Calcification')),
                ('assessment', models.CharField(choices=[('-1', 'UNKNOWN'), ('0', 'Category 0: Incomplete - Need Additional Imaging'), ('1', 'Category 1: Negative'), ('2', 'Category 2: Benign'), ('3', 'Category 3: Probably Benign'), ('Category 4: Suspicious', (('4A', 'Category 4A: Low suspicion for malignancy'), ('4B', 'Category 4B: Moderate suspicion for malignancy'), ('4C', 'Category 4C: High suspicion for malignancy'))), ('5', 'Category 5: Highly suggestive of malignancy'), ('6', 'Category 6: Known biopsy-proven malignancy')], max_length=10, verbose_name='Assessment')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('margin', models.ManyToManyField(to='labeling.BIRADSMarginChoice', verbose_name='Margin')),
            ],
        ),
    ]
