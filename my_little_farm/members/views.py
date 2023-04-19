from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    data = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    # return JsonResponse(data, encoder=DjangoJSONEncoder, safe=False)
    # return JsonResponse({
    #             'code': 200,
    #             'message': 'OK',
    #             'data': {
    #                 data
    #             }
    #         })
    return HttpResponse(template.render(context, request))
    # return HttpResponse(mymember.call_me())
    # return JsonResponse(serializers.serialize("json", [mymember]), encoder=DjangoJSONEncoder, safe=False)
    # return HttpResponse(json.dumps({'success':True, 'error': 'You need to login First'}))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple",],
    }
    return HttpResponse(template.render(context, request))
