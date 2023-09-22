from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_auto_20200729_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('Bachloar', 'Bachloar Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]
