from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Author)

admin.site.register(Search_keyword)
admin.site.register(Base_keyword)
admin.site.register(Introduce_Keyword)
admin.site.register(Fee_Keyword)

admin.site.register(Search_article)
admin.site.register(Base_article)
admin.site.register(Introduce_content)
admin.site.register(Fee_content)

admin.site.register(Join_form)
admin.site.register(Friend_link)
admin.site.register(Img_all)
admin.site.register(Index_img)
admin.site.register(Page_content)
# admin.site.register(Page_text)