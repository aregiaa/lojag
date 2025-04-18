# Generated by Django 5.0.2 on 2024-03-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='static/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
