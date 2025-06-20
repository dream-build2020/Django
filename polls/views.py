from django.http import HttpResponse
from django.template import loader

from polls.models import Job, Cities


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def joblist(request):
    jobs = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'jobs': jobs}

    for job in jobs:
        job.job_city = Cities[job.job_city]

    return HttpResponse(template.render(context))