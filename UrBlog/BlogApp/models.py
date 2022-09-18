from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.html import format_html

#--- Category ---

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=HTMLField()
    url=models.CharField(max_length=100)
    cat_image=models.ImageField(upload_to='card_images/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:80px; height:80px; border-radius:50%;"/>'.format(self.cat_image))
 
    def __str__(self):
        return self.title

#--- Post ---

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=HTMLField()
    url=models.CharField(max_length=100)
    post_image=models.ImageField(upload_to='post_images/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)


    def image_tag_post(self):
        return format_html('<img src="/media/{}" style="width:80px; height:80px; border-radius:50%;"/>'.format(self.post_image))

    def __str__(self):
        return self.title

# --- carosuel ---
class Carosuel(models.Model):
    carosuel_id=models.AutoField(primary_key=True)
    carosuel_image=models.ImageField(upload_to='carosuel_images/')

    def image_tag_carosuel(self):
        return format_html('<img src="/media/{}" style=" width:70%; height:400px; "/>'.format(self.carosuel_image))

# --- Comment ---

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    message=models.TextField()
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post_date=models.DateTimeField(auto_now_add=True)


# ---- Likes ----

class Like(models.Model):
    log_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    particular_user=models.ForeignKey(User,on_delete=models.CASCADE)
    like_btn=models.BooleanField(default=False)
    like_on=models.DateTimeField()

class Dislike(models.Model):
    log_post_d=models.ForeignKey(Post,on_delete=models.CASCADE)
    particular_user_d=models.ForeignKey(User,on_delete=models.CASCADE)
    like_btn_d=models.BooleanField(default=False)
    like_on_d=models.DateTimeField()


      