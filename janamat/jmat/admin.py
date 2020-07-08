from django.contrib import admin
from .models import *


admin.site.site_title = "MySite Admin"
admin.site.site_header = "Site Admin"
admin.site.index_title = "Site content"


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image', 'phone', 'dob', 'usr_type',)


admin.site.register(UserProfile, UserProfileAdmin)


class ChellengeAdmin(admin.ModelAdmin):
    list_display = ('chellengeName', 'chellengeDesc')


admin.site.register(Chellenge, ChellengeAdmin)


# class TopicListAdmin(admin.ModelAdmin):
#     list_display = ('Chellenge', 'Topic', 'TopicDesc', 'voteCount')


# admin.site.register(TopicList, TopicListAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'chellenge_id', 'date_comment', 'message')


admin.site.register(Comment, CommentAdmin)


# class VoteAdmin(admin.ModelAdmin):
#     list_display = ('Chellenge', 'Topic', 'User', 'is_votted')


# admin.site.register(Vote, VoteAdmin)


class contact_usAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'date')


admin.site.register(contact_us, contact_usAdmin)
