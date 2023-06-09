from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template import loader
from .models import Farmer, Cow

# Create your views here.
def farmers(request):
    mymembers = Farmer.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Farmer.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))
    # return JsonResponse(serializers.serialize("json", [mymember]), encoder=DjangoJSONEncoder, safe=False)


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple",],
    }
    return HttpResponse(template.render(context, request))
