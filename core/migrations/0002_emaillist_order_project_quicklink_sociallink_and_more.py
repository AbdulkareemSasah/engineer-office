# Generated by Django 4.2.1 on 2023-05-13 04:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("name", models.CharField(max_length=50)),
                ("phone", models.PositiveIntegerField()),
                (
                    "type_service",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("name_en", models.CharField(blank=True, max_length=500, null=True)),
                ("img", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                (
                    "body",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "body_en",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuickLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                ("name_en", models.CharField(blank=True, max_length=20, null=True)),
                ("url", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "verbose_name": "روابط الشريط العلوي",
            },
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "app",
                    models.CharField(
                        choices=[
                            ("facebook", "facebook"),
                            ("instagram", "instagram"),
                            ("twitter", "twitter"),
                            ("Linkedin", "Linkedin"),
                        ],
                        max_length=50,
                    ),
                ),
                ("link", models.CharField(max_length=750)),
            ],
        ),
        migrations.AddField(
            model_name="information",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="description_en",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="is_page",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="keywords",
            field=models.ManyToManyField(blank=True, null=True, to="core.keyword"),
        ),
        migrations.AlterField(
            model_name="article",
            name="post",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="post_en",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title_en",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="catagury",
            name="catagury",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="catagury",
            name="catagury_en",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="catagury",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="catagury",
            name="img_size",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="TimeOfWork",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="YearsOfExperience",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="information",
            name="location",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="logo_black",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="information",
            name="logo_color",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="information",
            name="logo_white",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="information",
            name="name_en",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="information",
            name="phoneNumber",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="keyword",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="keyword_en",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="navlink",
            name="name",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="navlink",
            name="name_en",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="navlink",
            name="url",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name="img_project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
            ],
        ),
    ]