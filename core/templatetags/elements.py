from django import template
from django.shortcuts import get_object_or_404, get_list_or_404

from core.forms import EmailListForm
from core.models import NavLink,SocialLink,Information,QuickLink
register = template.Library()

@register.inclusion_tag('theme/include/navbar.html')
def navlink():
    info = Information.objects.first()
    links = NavLink.objects.filter(active=True)
    context = {
        'informations': info,
        'links':links
    }
    return context



@register.inclusion_tag('theme/include/toolbar.html')
def toolbar():
    info = Information.objects.first()
    sociallinks = SocialLink.objects.filter(active=True)
    context = {
        'informations': info,
        'sociallinks':sociallinks
    }
    return context

@register.inclusion_tag('theme/include/footer.html')
def footer():
    info = Information.objects.first()
    sociallinks = SocialLink.objects.filter(active=True)
    quicklinks = QuickLink.objects.filter(active=True)
    form = EmailListForm()
    context = {
        'informations': info,
        'sociallinks':sociallinks,
        'quicklinks':quicklinks,
        'form':form,
    }
    return context