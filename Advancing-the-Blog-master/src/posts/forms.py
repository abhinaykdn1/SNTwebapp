from django import forms

from pagedown.widgets import PagedownWidget
from django.utils import timezone
from .models import Post


# tag_choices = ('SNT Council', 'Games and Sports', 'Cultural')
tag_choices = (
    ('SNT Council', 'SNT Council'),
    ('Games and Sports', 'Games and Sports'),
    ('Cultutal Council', 'Cultutal Council'),
)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    tags = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=tag_choices,)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
            "tags",
        ]