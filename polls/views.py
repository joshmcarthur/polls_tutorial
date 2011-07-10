from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll

def index(request):
    polls = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_polls': polls})
    # Note: render_to_response is a shortcut for lines 8..12 below
    #t = loader.get_template("polls/index.html")
    #c = Context({
    #    'latest_polls': polls
    #})
    #return HttpResponse(t.render(c))
        
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
    
def results(request, poll_id):
    return HttpResponse("You're looking at the results of %s" % poll_id)
    
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
    
