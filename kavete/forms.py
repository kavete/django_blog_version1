from django import forms

from kavete.models import BlogPost, Tag


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'content', 'preview_image', 'tags']
        exclude = ['author', 'date_published', 'date_updated']
        tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
        )
        labels = {
            'title': 'Title',
            'category': 'Category',
            'preview_image': 'Preview Image',
            'tags': 'Tags',
        }