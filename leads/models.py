from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", null=True, on_delete=models.SET_NULL)
    agent = models.ForeignKey("Agent", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    )

    id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPES
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    transaction_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_delayed = models.BooleanField(default=False)
    delay_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'

    def save(self, *args, **kwargs):
        if self.due_date and self.transaction_date > self.due_date:
            self.is_delayed = True
            self.delay_days = (self.transaction_date - self.due_date).days
        else:
            self.is_delayed = False
            self.delay_days = 0
        super().save(*args, **kwargs)