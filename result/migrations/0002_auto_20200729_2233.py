from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='session',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
