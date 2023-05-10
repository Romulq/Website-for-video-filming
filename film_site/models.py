from django.db import models
import datetime
from cloudinary.models import CloudinaryField


class VideoType(models.Model):
    name = models.CharField(verbose_name='Вид съемки', max_length=255)
    price = models.PositiveIntegerField(default=0, verbose_name='Цена', help_text='руб/час')
    slug = models.SlugField(default='type', verbose_name='Короткое название (на англ.)', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид съемки'
        verbose_name_plural = 'Виды съемки'


class Hashtags(models.Model):
    name = models.CharField(verbose_name='Хештег', max_length=255)
    slug = models.SlugField(default='type', verbose_name='Короткое название (на англ.)', max_length=32)
    videos = models.ManyToManyField('MyWorks', verbose_name='Видео ролики', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'

class MyWorks(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название видеоролика')
    videoType = models.ForeignKey(VideoType, on_delete=models.CASCADE, verbose_name='Виды съемки видеоролика')
    hashtag = models.ManyToManyField(Hashtags, verbose_name="Хештеги")
    videoFile = CloudinaryField('Видеоролик', resource_type='video')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мою работу'
        verbose_name_plural = 'Мои работы'


class AboutMe(models.Model):
    firstName = models.CharField(max_length=255, verbose_name='Твое имя')
    lastName = models.CharField(max_length=255, verbose_name='Твоя фамилия')
    selfy = models.ImageField(upload_to='image/', null=True, verbose_name='Аватар')
    description = models.TextField(blank=False, max_length=511, verbose_name='Немного о себе')

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class Order(models.Model):
    firstName = models.CharField(max_length=255, verbose_name='Имя заказчика')
    lastName = models.CharField(max_length=255, verbose_name='Фамилия заказчика')
    eventDate = models.DateField(verbose_name='Дата съемок')
    eventTime = models.TimeField(default=datetime.time(00, 00), verbose_name='Время начала съемок')
    typeVideo = models.ForeignKey(VideoType, on_delete=models.CASCADE, verbose_name='Вид съемки')
    timeWork = models.PositiveIntegerField(default=0, verbose_name='Длительность съемки (ч)')
    suggestions = models.TextField(blank=True, max_length=511, verbose_name='Пожелания заказчика')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона заказчика', blank=True)
    email = models.EmailField(max_length=127, verbose_name='Email заказчика')
    price = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name='Цена', help_text='рублей')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')

    def get_full_name(self):
        return self.lastName + ' ' + self.firstName

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

