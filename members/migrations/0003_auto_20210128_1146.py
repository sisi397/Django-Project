# Generated by Django 3.1.5 on 2021-01-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210127_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=128, verbose_name='상품이름')),
                ('price', models.CharField(max_length=64, verbose_name='가격')),
                ('images', models.CharField(max_length=64, verbose_name='이미지파일')),
                ('type', models.CharField(max_length=64, verbose_name='종류')),
            ],
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': '이용고객'},
        ),
        migrations.AlterModelTable(
            name='members',
            table='store user',
        ),
    ]