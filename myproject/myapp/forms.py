from django import forms

from myapp.models import Comment, Product, Tag


class AddProductForm(forms.ModelForm):
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(label='URL', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 58, 'rows': 10}))
    video = forms.CharField(label='Ссылка на видео с YouTube', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(label='Тег', queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ('title', 'slug', 'content', 'video', 'tags')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = Comment
        fields = ('content',)
