# myapp/templatetags/myapp_tags.py
from django import template
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from sass.models import SubscriptionPlan
from web.models import Service as WebService, gtype, Client, worker, testmone, galry, faq, socilamedia_company, map
from blogg import models as blog
from news import models as news
from pro import models as project
from service import models as servic
from shop import models as sho
from django.db.models import Sum, F

register = template.Library()

@register.simple_tag
def get_orders_and_total(user_id):
    try:
        use = User.objects.get(id = user_id)
        client = sho.Client.objects.get(user=use)
        orders = sho.Order.objects.filter(Client=client, active=True, sold=False)
        total_price = orders.aggregate(
            total=Sum(F('quntity') * F('item__price'))
        )['total'] or 0
        return orders, total_price
    except Client.DoesNotExist:
        return [], 0

@register.simple_tag
def get_gtype():
    return gtype.objects.all()

@register.simple_tag
def get_subscription_plans():
    return SubscriptionPlan.objects.all()

@register.simple_tag
def get_servic_services():
    return servic.Service.objects.all().order_by('-id')

@register.simple_tag
def get_projects():
    return project.Project.objects.all().order_by('-id')

@register.simple_tag
def get_news():
    return news.News.objects.all().order_by('-id')

@register.simple_tag
def get_blogs():
    return blog.Blog.objects.all().order_by('-id')

@register.simple_tag
def get_web_services():
    return WebService.objects.all().order_by('-id')

@register.simple_tag
def get_clients():
    return Client.objects.all()

@register.simple_tag
def get_workers():
    return worker.objects.all()

@register.simple_tag
def get_testimonials():
    return testmone.objects.all().order_by('-id')


@register.simple_tag
def get_socialmedia():
    return socilamedia_company.objects.all().order_by('-id')

@register.simple_tag
def get_gallery():
    return galry.objects.all()


@register.simple_tag
def get_map():
    return map.objects.all().first()


@register.simple_tag
def get_faqs():
    return faq.objects.all()

@register.simple_tag
def get_items(page_number=1, items_per_page=10):
    all_items = sho.Item.objects.filter(active=True).order_by('-id')
    paginator = Paginator(all_items, items_per_page)
    return paginator.page(page_number)

@register.simple_tag
def get_types():
    return sho.Type.objects.all()
