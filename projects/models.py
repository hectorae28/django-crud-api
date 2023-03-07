from django.db import models


class MenuItems(models.Model):
    name = models.CharField(max_length=35, blank=False)
    description = models.TextField()
    price = models.IntegerField(blank=False)

    def __str__(self):
        """Return title and username."""
        return '{} a {}$'.format(self.name, self.price)


class Products(models.Model):
    isSell = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    menu_item = models.ForeignKey(
        'MenuItems',
        on_delete=models.CASCADE,
        related_name='product_menuitem'
    )
    order = models.ForeignKey(
        'Orders',
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        """Return title and username."""
        return '{}, Vendido: {},fecha {}'.format(self.menu_item.name, self.isSell, self.date_create)


class Orders(models.Model):
    name = models.CharField(max_length=35, blank=False)
    last_name = models.CharField(max_length=35)
    nota = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    isPayed = models.BooleanField(default=False)
    payment_type_choise = [('PM', 'Pago movil'), ('EF', 'Efectivo'),]
    payment_type = models.CharField(
        max_length=35, blank=True, choices=payment_type_choise, null=True)

    def __str__(self):
        """Return title and username."""
        return 'num {} de {}, Pagado: {}'.format(self.id, self.name, self.isPayed)
