from django.contrib import admin
from .models import Carosuel, Category,Post,Carosuel,Comment,Like,Dislike

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['image_tag','title','description','add_date']
    search_fields=['title']
    

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display=['image_tag_post','title','category','url','content','add_date']
    search_fields=['title']
    list_filter=['category']
    list_per_page=5

@admin.register(Carosuel)
class Carosuel_Admin(admin.ModelAdmin):
    list_display=['image_tag_carosuel']

@admin.register(Comment)
class Comment_Admin(admin.ModelAdmin):
    list_display=['id','post','message','post_date']

@admin.register(Like)
class Liked_Admin(admin.ModelAdmin):
  list_display=['log_post','particular_user','like_on','like_btn']

@admin.register(Dislike)
class Disliked_Admin(admin.ModelAdmin):
  list_display=['log_post_d','particular_user_d','like_on_d','like_btn_d']