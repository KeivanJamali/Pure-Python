import string

from django.core.exceptions import ValidationError
from django.db import models


def validate_username(value):
    if type(value) == str:
        if len(value) < 5 or len(value) > 20:
            raise ValidationError("invalid username")
        n = False
        for char in value:
            if char not in string.ascii_letters and char not in string.digits and char not in "_":
                raise ValidationError("invalid username")
            if char.isalpha():
                n = True

        if not n:
            raise ValidationError("invalid username")

        return
    raise ValidationError("invalid username")


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, validators=[validate_username])
    private = models.BooleanField(default=False)
    followings = models.ManyToManyField('User', related_name='followers', blank=True)
    outgoing_follow_requests = models.ManyToManyField('User', related_name='incoming_follow_requests', blank=True)

    def follow(self, other_user):
        if other_user != self and not self.follows_user(other_user):
            if other_user.private:
                self.send_follow_request(other_user)
            else:
                self.followings.add(other_user)
                other_user.followers.add(self)

    def unfollow(self, other_user):
        if other_user != self and self.follows_user(other_user):
            self.followings.remove(other_user)
            other_user.followers.remove(self)

    def remove_follower(self, other_user):
        if other_user in self.followers.all():
            self.followers.remove(other_user)
            other_user.followings.remove(self)

    def remove_request(self, other_user):
        if other_user in self.incoming_follow_requests.all():
            self.incoming_follow_requests.remove(other_user)
            other_user.outgoing_follow_requests.remove(self)

    def accept_request(self, other_user):
        if other_user in self.incoming_follow_requests.all():
            self.incoming_follow_requests.remove(other_user)
            self.followings.add(other_user)
            other_user.followers.add(self)

    def refuse_request(self, other_user):
        if other_user in self.incoming_follow_requests.all():
            self.incoming_follow_requests.remove(other_user)
            other_user.outgoing_follow_requests.remove(self)

    def create_post(self, text):
        if self.is_valid_text(text):
            post = Post.objects.create(text=text, owner=self)
            return post

    def like(self, post):
        if post not in self.liked_posts.all():
            self.liked_posts.add(post)
            self.disliked_posts.remove(post)

    def dislike(self, post):
        if post not in self.disliked_posts.all():
            self.disliked_posts.add(post)
            self.liked_posts.remove(post)

    def clear_vote(self, post):
        if post in self.liked_posts.all() or post in self.disliked_posts.all():
            self.liked_posts.remove(post)
            self.disliked_posts.remove(post)

    def follows_user(self, other_user):
        return other_user in self.followings.all()

    def send_follow_request(self, other_user):
        if other_user not in self.outgoing_follow_requests.all():
            self.outgoing_follow_requests.add(other_user)
            other_user.incoming_follow_requests.add(self)

    def is_valid_text(self, text):
        return len(text) >= 5 and len(text) <= 255


class Post(models.Model):
    text = models.CharField(max_length=255)
    posted_time = models.DateTimeField(auto_now_add=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    disliked_users = models.ManyToManyField(User, related_name='disliked_posts')

    def __str__(self):
        return self.text
