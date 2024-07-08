from django.shortcuts import render

from django.http import HttpResponse# envoyer une reponse http

from django.template import loader # chargeur de template


def index (request):

    context={"message" :" hello world!!"} # injecter des valeurs ds le template
    template= loader.get_template("mangalib/index.html") # recuperer le fichier du template 
    return HttpResponse(template.render(context, request))