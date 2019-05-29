from django.shortcuts import render, get_object_or_404
from django.views.generic import View


from .models import *


def pollsList(request):
    allPolls = list(Poll.objects.all())
    polls = []
    alreadyAdded = 0

    while len(allPolls) - 2 >= alreadyAdded:
        curPolls = []
        curPolls.append(allPolls[alreadyAdded])
        curPolls.append(allPolls[alreadyAdded + 1])

        alreadyAdded += 2
        polls.append(curPolls)
    if alreadyAdded != len(allPolls):
        curPolls = []
        for i in range(alreadyAdded, len(allPolls)):
            curPolls.append(allPolls[alreadyAdded])
            alreadyAdded += 1
        polls += [curPolls]
    print()
    print(polls)
    print()
    polls = list(polls)
    return render(request, 'pollCore/pollsList.html', context={'polls': polls})


def mainPage(request):
    return render(request, 'pollCore/mainPage.html')


class PollDetail(View):
    def get(self, request, slug):
        poll = Poll.objects.get(slug__iexact=slug)
        return render(request, 'pollCore/pollDetail.html', context={'poll': poll})