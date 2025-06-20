from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=200, verbose_name='旅行名')
    start_date = models.DateField(verbose_name='開始日', null=True, blank=True)
    end_date = models.DateField(verbose_name='終了日', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 機能1: 予約管理モデル
class Reservation(models.Model):
    class ReservationType(models.TextChoices):
        HOTEL = 'HTL', 'ホテル'
        FLIGHT = 'FLT', 'フライト'
        TRAIN = 'TRN', '電車'
        TOUR = 'TOR', 'ツアー'
        OTHER = 'OTH', 'その他'

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reservations')
    reservation_type = models.CharField(max_length=3, choices=ReservationType.choices, default=ReservationType.OTHER, verbose_name='予約の種類')
    name = models.CharField(max_length=200, verbose_name='予約対象の名称')
    start_datetime = models.DateTimeField(verbose_name='開始日時')
    end_datetime = models.DateTimeField(verbose_name='終了日時', null=True, blank=True)
    location = models.CharField(max_length=300, blank=True, verbose_name='場所/住所')
    confirmation_number = models.CharField(max_length=100, blank=True, verbose_name='予約番号')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='金額')
    source_text = models.TextField(blank=True, verbose_name='元のテキスト')

    class Meta:
        ordering = ['start_datetime']

# 機能2: 出費管理モデル
class Expense(models.Model):
    class ExpenseCategory(models.TextChoices):
        FOOD = 'FOOD', '食費'
        TRANSPORT = 'TRANS', '交通費'
        LODGING = 'LODGE', '宿泊費'
        SIGHTSEEING = 'SIGHT', '観光'
        SHOPPING = 'SHOP', 'お土産・買い物'
        OTHER = 'OTHER', 'その他'

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='金額')
    category = models.CharField(max_length=5, choices=ExpenseCategory.choices, verbose_name='カテゴリ')
    expense_date = models.DateField(verbose_name='日付')
    notes = models.CharField(max_length=255, blank=True, verbose_name='メモ')
    currency = models.CharField(max_length=10, default='JPY', verbose_name='通貨')
    payment_method = models.CharField(max_length=50, blank=True, verbose_name='支払い方法')

    class Meta:
        ordering = ['-expense_date']

# 機能3: 旅の予定（タイムライン）モデル
class ItineraryItem(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itinerary_items')
    start_time = models.DateTimeField(verbose_name='開始時間')
    end_time = models.DateTimeField(verbose_name='終了時間', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='予定のタイトル')
    location = models.CharField(max_length=300, blank=True, verbose_name='場所')
    notes = models.TextField(blank=True, verbose_name='メモ')
    related_reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='関連する予約')

    class Meta:
        ordering = ['start_time']

# 機能4: ToDoリストの「カテゴリ」モデル
class TodoCategory(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='todo_categories')
    name = models.CharField(max_length=100, verbose_name='カテゴリ名')

    def __str__(self):
        return self.name

# 機能4: ToDoリストの「アイテム」モデル
class TodoItem(models.Model):
    category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE, related_name='items')
    task = models.CharField(max_length=255, verbose_name='タスク内容')
    is_completed = models.BooleanField(default=False, verbose_name='完了フラグ')

    class Meta:
        ordering = ['is_completed']