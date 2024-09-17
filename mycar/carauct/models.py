from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import PositiveSmallIntegerField, DecimalField
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    country = models.CharField(max_length=33)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', blank=True)

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):
    category_name = models.CharField(max_length=33, unique=True)

    def __str__(self):
        return f'{self.category_name}'

class CarMake(models.Model):
    car_make_name = models.CharField(max_length=33, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_make_name}'

class Model(models.Model):
    model_name = models.CharField(max_length=33, unique=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_make} - {self.model_name}'

class Car(models.Model):
    car_name = models.CharField(max_length=33)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Car_Make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)
    add_date = models.DateField(verbose_name='Время', auto_now_add=True)
    city = models.CharField(max_length=33)
    country = models.CharField(verbose_name='Страна', max_length=33)
    mileage = models.PositiveSmallIntegerField(verbose_name='Пробег', default=0)
    image = models.ImageField(upload_to='машины/', blank=True, null=True)
    with_photo = models.BooleanField(default=True)
    CHOICES_DRIVE = (
        ("задний", "ЗАДНИЙ"),
        ("передний", "ПЕРЕДНИЙ"),
        ("полный", "ПОЛНЫЙ"),
    )
    drive = models.CharField(verbose_name='Привод', max_length=33, choices=CHOICES_DRIVE)
    CHOICES_ENGINE = (
        ("бензин", "БЕНЗИН"),
        ("газ", "ГАЗ"),
        ("дизель", "ДИЗЕЛЬ"),
        ("электро", "ЭЛЕКТРО"),
        ("гибрид", "ГИБРИД"),
    )
    engine = models.CharField(verbose_name='Топливо', max_length=33, choices=CHOICES_ENGINE)
    CHOICES_TRANSMISSION = (
        ("механика", "МЕХАНИКА"),
        ("автомат", "АВТОМАТ"),
        ("вариатор", "ВАРИАТОР"),
        ("робот", "РОБОТ"),
    )
    transmission = models.CharField(verbose_name='Коробка', max_length=33, choices=CHOICES_TRANSMISSION)
    volume = models.FloatField(default=0.8)

    def __str__(self):
        return f'{self.car_name}'

class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='auctions')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.car} - {self.end_date}'

class Bid(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ставка {self.user} на сумму {self.amount}'

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Заказ по {self.user} на {self.car}'

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('в ожидании', 'В ОЖИДАНИИ'), ('завершеннный', 'ЗАВЕРШЕННЫЙ')])

    def __str__(self):
        return f'Оплата за {self.order} - {self.status}'

class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.author} - {self.car}'