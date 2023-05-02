from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from datetime import date

from .terms_work import compare
from .terms_work import try_to_add_picture


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})

def terms_list_with_pic(request):
    terms_with_pic = terms_work.get_terms_for_table_with_pic()
    return render(request, "term_list.html", context={"terms_with_pic": terms_with_pic})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        elif compare(new_term) == False:
            context["success"] = False
            context["comment"] = "Данное слово уже записано в словарь"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition, date.today())
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def add_term_picture(request):
    if request.method == "POST":
        cache.clear()
        old_term = request.POST.get("old_term", "")
        add_picture = request.POST.get("add_picture", "")
        user_name = 'Полиглот'
        context = {"user": user_name}
        if len(add_picture) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли вставить ссылку на картинку :("
        elif len(old_term) == 0:
            context["success"] = False
            context["comment"] = "Вы не ввели слово, к которому хотите добавить картинку"
        elif try_to_add_picture(old_term) == False:
            context["success"] = False
            context["comment"] = "Слово, к которому вы пытаетесь добавить картинку, отсутсвует в словаре"
        else:
            context["success"] = True
            context["comment"] = "Ваша картинка принята"
            terms_work.add_picture_to_term(old_term, add_picture)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request_2.html", context)
    else:
        add_term_pic(request)

def add_term_pic(request):
    return render(request, "term-add-picture.html")

def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
