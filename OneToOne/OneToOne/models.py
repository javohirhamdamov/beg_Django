from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Turkum'
        verbose_name_plural = 'Turkumlar'
        

class Number(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = 'id'
        verbose_name_plural = 'idlar'
        

class Maqola(models.Model):
    class Vil(models.IntegerChoices):
        Tash = '1', 'Tashkent',
        Bux = '2', 'Buxoro',
        Qar = '3', 'Qarshi',
        __empty__ = 'Viloyatni tanlang'
    
    title = models.CharField(max_length=25)
    content = models.TextField()
    author = models.CharField('Yozuvchi', max_length=15)
    is_publishet = models.BooleanField('Chop etilganmi')
    Viloyat = models.SmallIntegerField(choices=Vil.choices)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    num = models.OneToOneField(Number, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
    
    
