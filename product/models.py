from datetime import datetime
from email.policy import default
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from settings.models import Brand,Variant
from django.urls import reverse



# Create your models here.
# MODEL ITEM
class Item(models.Model):
    name = models.CharField(max_length=50,verbose_name=_('Product name'))
    category = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey('settings.Brand', verbose_name=_("Brand"), on_delete=models.CASCADE,null=True,blank=True)
    # variant = models.ForeignKey(Variant, verbose_name=_("Variant"), on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField(verbose_name=_('Product price'))
    discount_price = models.IntegerField(verbose_name=_("Discount_price"),null=True,blank=True)
    image = models.ImageField(upload_to='Images_items/%y/%m/%d',verbose_name=_('Product image'),null=True,blank=True)
    description = models.TextField(verbose_name=_('Product description'))
    created_at = models.DateTimeField(default=datetime.now,verbose_name=_('Product created at'))
    slug = models.SlugField(null=True,blank=True,verbose_name=' slug')


    def save(self,*args,**kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Item,self).save(*args,**kwargs)

    
    def get_absolute_url(self):
        return reverse('product:product_detail',kwargs={'slug':self.slug})
    


    def __str__(self) :
        return self.name

class ItemImage(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    ITIImage = models.ImageField(upload_to='Images_items/%y/%m/%d',verbose_name='Product image')


    def __str__(self) :
        return str(self.item)


# MODEL CATEGORY
class Category(models.Model):
    CATName = models.CharField(max_length=100,verbose_name=_('Category'))
    CATParent = models.ForeignKey('self',limit_choices_to={'CATParent__isnull':True},on_delete=models.CASCADE,null=True,blank=True,verbose_name=_('Main Category'))#عشان افلترها واعمل علاه مع ال مالوش اب فبقوله ال النل بتاعت فاضيه يبقا دا الاب وبخليه يعمل علاقه عكسيه مع نفسه 
    CATDesc = models.TextField(verbose_name=_('Description'),null=True,blank=True)
    CATImage = models.ImageField(upload_to='Images_categories/%y/%m/%d',verbose_name='Category Image',null=True,blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self) :
        return self.CATName

class Item_Alternative(models.Model): #البدائل الخاصه بالمنتج
    ITALName = models.ForeignKey(Item,related_name='Item_Name', on_delete=models.CASCADE,verbose_name=_('Item'))
    ITALAlternative = models.ManyToManyField(Item,related_name='Item_Alternative',verbose_name=_('Alternatives' ))

    

    class Meta:
        verbose_name = _("Item Alternative")
        verbose_name_plural = _("Items AlternatIives")

    def __str__(self):
        return str(self.ITALName)

class Item_Accessories(models.Model):
    ITACCName = models.ForeignKey(Item,related_name='Item_Name_ACC', on_delete=models.CASCADE,verbose_name=_('Item'))
    ITACCAlternative = models.ManyToManyField(Item,related_name='Item_Accessories',verbose_name=_('Accessories'))
    

    class Meta:
        verbose_name = _("Item Accessory")
        verbose_name_plural = _("Items Accessories")

    def __str__(self):
        return str(self.ITACCName)



