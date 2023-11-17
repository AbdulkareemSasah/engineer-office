from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.translation import get_language



class Keyword(models.Model):
    keyword = models.CharField(max_length=50, null=True, blank=True)
    keyword_en = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def keyword_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.keyword
        else:
            return self.keyword_en

    def __str__(self):
        return self.keyword



class Information(models.Model):
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    logo_color = models.ImageField(null=True, blank=True)
    logo_white = models.ImageField(null=True, blank=True)
    logo_black = models.ImageField(null=True, blank=True)
    phoneNumber = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    TimeOfWork = models.CharField(max_length=100, null=True, blank=True)
    YearsOfExperience = models.PositiveIntegerField(null=True, blank=True)
    keyword = models.ManyToManyField(Keyword,blank=True)

    @property
    def name_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.name
        else:
            return self.name_en

    @property
    def description_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.description
        else:
            return self.description_en

    class Meta:
        verbose_name = "معلومات المكتب"


class NavLink(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    name_en = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def name_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.name
        else:
            return self.name_en

    class Meta:
        verbose_name = "روابط الشريط العلوي"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('url').choices = self.get_choices()


    def __str__(self):
        return f'{self.name} to {self.url}'

    def get_choices(self):
        choices = []
        articles = Article.objects.filter(active=True,is_page=True)
        for article in articles:
            url_path = article.title
            url_name = article.title  # اسم الخيار المعروض في ChoiceField
            choices.append((url_path, url_name))

        choices.append(('/', "home"))
        return choices


class QuickLink(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    name_en = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def name_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.name
        else:
            return self.name_en

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "روابط الشريط السفلي"


class Catagury(models.Model):
    catagury = models.CharField(max_length=50, null=True, blank=True)
    catagury_en = models.CharField(max_length=50, null=True, blank=True)
    head = models.CharField(max_length=50, null=True, blank=True)
    head_en = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    img_size = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def catagury_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.catagury
        else:
            return self.catagury_en

    @property
    def head_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.head
        else:
            return self.head_en
    def __str__(self):
        return self.catagury

    class Meta:
        verbose_name = "اقسام الفقرات"


class Article(models.Model):
    catagury = models.ForeignKey(Catagury, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    title_en = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    description_en = models.CharField(max_length=1000, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    post = RichTextUploadingField(null=True, blank=True)
    post_en = RichTextUploadingField(null=True, blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    is_page = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def title_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.title
        else:
            return self.title_en

    @property
    def description_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.description
        else:
            return self.description_en

    @property
    def post_display(self):
        lang = get_language()
        if lang == 'ar':
            return self.post
        else:
            return self.post_en
    def __str__(self):
        return f' { self.title} - {self.catagury.catagury}'

    class Meta:
        verbose_name = "الفقرات"




class Order(models.Model):
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    type_service = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.type_service}'


class EmailList(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    choices = [
        ("facebook", "facebook"),
        ("instagram", "instagram"),
        ("twitter", "twitter"),
        ("Linkedin", "Linkedin"),

    ]
    app = models.CharField(choices=choices, max_length=50)
    link = models.CharField(max_length=750)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.app


class Project(models.Model):
    name = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    body_en = RichTextUploadingField(null=True, blank=True)
    active = models.BooleanField(default=False)
    @property
    def name_desplay(self):
        if get_language() == 'ar':
            return self.name
        else:
            return self.name_en

    @property
    def description_desplay(self):
        if get_language() == 'ar':
            return self.description
        else:
            return self.description_en

    @property
    def body_desplay(self):
        if get_language() == 'ar':
            return self.body
        else:
            return self.body_en

    def __str__(self):
        if get_language() == 'ar':
            return self.name
        else:
            return self.name_en


class img_project(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img = models.ImageField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.project.name
