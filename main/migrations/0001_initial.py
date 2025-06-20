# Generated by Django 5.2.3 on 2025-06-20 06:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoCategory",
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
                ("name", models.CharField(max_length=100, verbose_name="カテゴリ名")),
            ],
        ),
        migrations.CreateModel(
            name="TodoItem",
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
                ("task", models.CharField(max_length=255, verbose_name="タスク内容")),
                (
                    "is_completed",
                    models.BooleanField(default=False, verbose_name="完了フラグ"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="main.todocategory",
                    ),
                ),
            ],
            options={
                "ordering": ["is_completed"],
            },
        ),
        migrations.CreateModel(
            name="Trip",
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
                ("title", models.CharField(max_length=200, verbose_name="旅行名")),
                (
                    "start_date",
                    models.DateField(blank=True, null=True, verbose_name="開始日"),
                ),
                (
                    "end_date",
                    models.DateField(blank=True, null=True, verbose_name="終了日"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="todocategory",
            name="trip",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="todo_categories",
                to="main.trip",
            ),
        ),
        migrations.CreateModel(
            name="Reservation",
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
                    "reservation_type",
                    models.CharField(
                        choices=[
                            ("HTL", "ホテル"),
                            ("FLT", "フライト"),
                            ("TRN", "電車"),
                            ("TOR", "ツアー"),
                            ("OTH", "その他"),
                        ],
                        default="OTH",
                        max_length=3,
                        verbose_name="予約の種類",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="予約対象の名称"),
                ),
                ("start_datetime", models.DateTimeField(verbose_name="開始日時")),
                (
                    "end_datetime",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="終了日時"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="場所/住所"
                    ),
                ),
                (
                    "confirmation_number",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="予約番号"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="金額",
                    ),
                ),
                (
                    "source_text",
                    models.TextField(blank=True, verbose_name="元のテキスト"),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="main.trip",
                    ),
                ),
            ],
            options={
                "ordering": ["start_datetime"],
            },
        ),
        migrations.CreateModel(
            name="ItineraryItem",
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
                ("start_time", models.DateTimeField(verbose_name="開始時間")),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="終了時間"
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="予定のタイトル"),
                ),
                (
                    "location",
                    models.CharField(blank=True, max_length=300, verbose_name="場所"),
                ),
                ("notes", models.TextField(blank=True, verbose_name="メモ")),
                (
                    "related_reservation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.reservation",
                        verbose_name="関連する予約",
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itinerary_items",
                        to="main.trip",
                    ),
                ),
            ],
            options={
                "ordering": ["start_time"],
            },
        ),
        migrations.CreateModel(
            name="Expense",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="金額"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("FOOD", "食費"),
                            ("TRANS", "交通費"),
                            ("LODGE", "宿泊費"),
                            ("SIGHT", "観光"),
                            ("SHOP", "お土産・買い物"),
                            ("OTHER", "その他"),
                        ],
                        max_length=5,
                        verbose_name="カテゴリ",
                    ),
                ),
                ("expense_date", models.DateField(verbose_name="日付")),
                (
                    "notes",
                    models.CharField(blank=True, max_length=255, verbose_name="メモ"),
                ),
                (
                    "currency",
                    models.CharField(default="JPY", max_length=10, verbose_name="通貨"),
                ),
                (
                    "payment_method",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="支払い方法"
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses",
                        to="main.trip",
                    ),
                ),
            ],
            options={
                "ordering": ["-expense_date"],
            },
        ),
    ]
