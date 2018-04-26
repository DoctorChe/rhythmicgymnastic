from PyPDF2.pdf import BytesIO
from django.shortcuts import render, get_object_or_404

from .models import Gymnast

# import io
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

from django_xhtml2pdf.utils import generate_pdf
from django.http import HttpResponse


def protocolview(response):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('competitions/test_pdf.html', file_object=resp)
    return result

import operator


def competition(request):
    # gymnast_list_with_rank = [gymnast for gymnast in Gymnast.objects.all() if gymnast.rank_position]
    # gymnasts = gymnast_list_with_rank.sort(key=operator.attrgetter('rank_position'))
    # gymnasts = Gymnast.objects.filter(key=operator.attrgetter('rank_position')).sort(key=operator.attrgetter('rank_position'))
    # gymnasts = Gymnast.objects.filter(rank_position)
    gymnasts = [x for x in Gymnast.objects.all() if x.rank_position()]
    return render(request, 'competitions/competition.html', {'gymnasts': gymnasts})


# def competition_list(request):
#     competitions = Competition.start.all()
#     return render(request, 'competitions/competition/list.html', {'competitions': competitions})
#
#
# def competition_detail(request, year, month, competition):
#     competition = get_object_or_404(Competition,
#                                     slug=competition,
#                                     # status='published',
#                                     competition__year=year,
#                                     competition__month=month)
#     return render(request, 'competitions/competition/detail.html', {'competition': competition})


# def gymnast_list(request):
#     gymnasts = Gymnast.MSMK.all()
#     return render(request, 'competitions/gymnast/list.html', {'gymnasts': gymnasts})
#
#
# def gymnast_detail(request, year, month, gymnast):
#     gymnast = get_object_or_404(Gymnast,
#                                 slug=gymnast,
#                                 # status='published',
#                                 competition__year=year,
#                                 competition__month=month)
#     return render(request, 'competitions/gymnast/detail.html', {'gymnast': gymnast})


# from .models import Post
#
#
# # def post_list(request):
# #     posts = Post.published.all()
# #     return render(request, 'competitions/post/list.html', {'posts': posts})
#
#
# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                                    status='published',
#                                    publish__year=year,
#                                    publish__month=month,
#                                    publish__day=day)
#     return render(request, 'competitions/post/detail.html', {'post': post})
#
#
# from django.views.generic import ListView
#
#
# class PostListView(ListView):
#     queryset = Post.objects.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'competitions/post/list.html'


import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
# from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from .utils import extract_request_variables


# try:  # python2 and python3
#     from .utils import extract_request_variables
# except:
#     from utils import extract_request_variables


def index(request):
    return render(request, 'competitions/report/index.html')


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    # Typically /home/userX/project_static/media/
    mRoot = settings.MEDIA_ROOT

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def render_pdf(request):
    template_path = 'competitions/report/user_printer.html'
    context = extract_request_variables(request)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    # html = template.render(Context(context))
    html = template.render(context)
    if request.POST.get('show_html', ''):
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename="report.txt"'
        response.write(html)
    else:
        pisaStatus = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)
        if pisaStatus.err:
            return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,
                                                                                   html))
    return response


def fetch_pdf_resources(uri, rel):
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    elif uri.find(settings.STATIC_URL) != -1:
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    else:
        path = None
    return path


# def competition_pdf(request, id):
def competition_pdf(request):
    id=1
    from .models import Competition
    competition_print = get_object_or_404(Competition, pk=id)
    context = {'competition_print': competition_print, }
    # context = {}
    context = extract_request_variables(request)
    # context.update(extract_request_variables(request))
    template_path = 'competitions/report/competition_protocol_print.html'
    # template_path = 'competitions/report/user_printer.html'

    template = get_template(template_path)
    html  = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()

    # pdf = pisa.pisaDocument(BytesIO(template.encode('UTF-8')), result,
    #                         encoding='utf-8',
    #                         link_callback=fetch_pdf_resources)

    return HttpResponse(pdf, 'application/pdf')
    # return HttpResponse(result.getvalue(), mimetype='application/pdf')
