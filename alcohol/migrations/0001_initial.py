# Generated by Django 3.2.8 on 2021-10-17 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.uploading


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('metro', models.CharField(blank=True, max_length=50, null=True, verbose_name='ст. Метро')),
                ('street', models.CharField(max_length=300, verbose_name='Улица, дом, подъезд, квартира')),
                ('primary', models.BooleanField(default=True, verbose_name='Основной адрес?')),
            ],
            options={
                'verbose_name': 'Адрес покупателя',
                'verbose_name_plural': 'Адреса покупателей',
            },
        ),
        migrations.CreateModel(
            name='BottleVolume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Объем тары')),
            ],
            options={
                'verbose_name': 'Объем тары',
                'verbose_name_plural': 'Объемы тары',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Торговая марка')),
                ('slug', models.SlugField(unique=True, verbose_name='Псевдоним/Slug')),
                ('since_date', models.DateField(verbose_name='Дата основания')),
                ('description', models.TextField(default='Описание появится позже', verbose_name='Описание')),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
            ],
            options={
                'verbose_name': 'Торговая марка',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField(default=0, verbose_name='Общее кол-во товаров в корзине')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonimous_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины покупателей',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(unique=True, verbose_name='Псевдоним/Slug')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Страна')),
                ('slug', models.SlugField(unique=True, verbose_name='Псевдоним/Slug')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны производителей',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('phone', models.CharField(max_length=18, verbose_name='Номер телефона')),
                ('addresses', models.ManyToManyField(blank=True, related_name='addresses', to='alcohol.Address', verbose_name='Адрес покупателя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Список =покупателей',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Псевдоним/Slug')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('stock', models.IntegerField(default=1, verbose_name='Количество на складе')),
                ('description', models.TextField(default='Описание товара появится позже', verbose_name='Описание товара')),
                ('offer_of_the_week', models.BooleanField(default=False, verbose_name='Предложение недели')),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование рецепта')),
                ('description', models.TextField(verbose_name='Описание рецепта')),
                ('products', models.ManyToManyField(related_name='recipes', to='alcohol.Product', verbose_name='Напитки используемые для рецепта')),
            ],
            options={
                'verbose_name': 'Рецепт напитка/коктейля',
                'verbose_name_plural': 'Рецепты напитков/коктейлей',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alcohol.recipe', verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.bottlevolume', verbose_name='Объем'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=18, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('confirmed', 'Заказ подтвержден'), ('in_progress', 'Заказ в обработке'), ('ready', 'Заказ готов'), ('completed', 'Заказ получен покупателем'), ('cancelled', 'Заказ отменен')], default='new', max_length=100)),
                ('bying_type', models.CharField(choices=[('self', 'Самовывоз из магазина'), ('delivery', 'Доставка')], default='delivery', max_length=100)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateField(auto_now=True, verbose_name='дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Предпочитаемая дата получения заказа')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='alcohol.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ покупателя',
                'verbose_name_plural': 'Заказы покупателей',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст уведомления')),
                ('read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.customer', verbose_name='Получатель уведомления')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления дял пользователей',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='user_orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='alcohol.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='alcohol.Product', verbose_name='Лист ожидания'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.cart', verbose_name='Корзина')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.customer', verbose_name='Покупатель')),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Объем')),
            ],
            options={
                'verbose_name': 'Продукт корзины',
                'verbose_name_plural': 'Продукты корзины',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='alcohol.CartProduct', verbose_name='Товары в корзине'),
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ManyToManyField(related_name='brands', to='alcohol.Category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='brand',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.country', verbose_name='Страна происхождения'),
        ),
        migrations.AddField(
            model_name='brand',
            name='products',
            field=models.ManyToManyField(related_name='products', to='alcohol.Product', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alcohol.customer', verbose_name='Покупатель'),
        ),
    ]