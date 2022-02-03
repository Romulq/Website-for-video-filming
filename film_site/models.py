from django.db import models


class VideoType(models.Model):
    name = models.CharField(verbose_name='Тип съемки', max_length=255)
    price = models.PositiveIntegerField(default=0, verbose_name='Цена', help_text='руб/час')
    slug = models.SlugField(default='type', verbose_name='Короткое название (на англ.)', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип съемки'
        verbose_name_plural = 'Типы съемки'


class MyWorks(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название видеоролика')
    videoType = models.ForeignKey(VideoType, on_delete=models.CASCADE, verbose_name='Типы съемки видеоролика')
    videoFile = models.FileField(upload_to='videos/', null=True, verbose_name='Видеоролик')

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
    typeVideo = models.ForeignKey(VideoType, on_delete=models.CASCADE, verbose_name='Тип съемки')
    timeWork = models.PositiveIntegerField(default=0, verbose_name='Время съемки', help_text='часов')
    suggestions = models.TextField(blank=True, max_length=511, verbose_name='Пожелания заказчика')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона заказчика', blank=True)
    email = models.EmailField(max_length=127, verbose_name='Email заказчика')
    price = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name='Итоговая цена заказа', help_text='рублей')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
