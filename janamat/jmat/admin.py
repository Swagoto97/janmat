from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display= ('user', 'profile_image', 'phone', 'dob', 'usr_type',)
admin.site.register(UserProfile, UserProfileAdmin)

class ChellengeAdmin(admin.ModelAdmin):
    list_display= ('chellengeName', 'chellengeDesc')
admin.site.register(Chellenge, ChellengeAdmin)

class TopicListAdmin(admin.ModelAdmin):
    list_display= ('Chellenge', 'Topic', 'TopicDesc', 'voteCount')
admin.site.register(TopicList, TopicListAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display= ('user_id', 'chellenge_id', 'date_comment', 'message', 'updated_by')
admin.site.register(Comment, CommentAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display= ('Chellenge', 'Topic', 'User', 'is_votted')
admin.site.register(Vote, VoteAdmin)
