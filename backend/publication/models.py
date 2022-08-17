from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    cat = models.CharField('Category', max_length=100, unique=True)

    def __str__(self):
        return self.cat

    class Meta:
        db_table = 'publication_category'    
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('cat',)

class PublicationModel(models.Model):
    cat = models.ForeignKey(
        CategoryModel,
        to_field='cat',
        related_name='Сategories', 
        on_delete=models.CASCADE,
        blank=True,
    )
    owner = models.ForeignKey(
        User, related_name='Creaters', 
        on_delete=models.PROTECT, default=1
    )
    title = models.CharField('Title', max_length=100)
    img = models.ImageField('background', upload_to='publication_bg_img/', blank=True)
    content = models.TextField('Content')
    created_at = models.DateTimeField('Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField('Date of update', auto_now=True)
    is_published = models.BooleanField('Publihed', default=True)
                                    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'publication'
        verbose_name = 'Publocation'
        verbose_name_plural = 'Publocations'
        ordering = ('-created_at',)

    