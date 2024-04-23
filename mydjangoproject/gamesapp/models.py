from django.db import models


# Создайте модель для запоминания бросков монеты: орёл или решка.Также запоминайте время броска
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей - значений, для орла и для решки

class Coin(models.Model):
    name = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_n_coins(n):
        return Coin.objects.order_by('-time')[:n]

    def __str__(self):
        return self.name + ' ' + str(self.time)
