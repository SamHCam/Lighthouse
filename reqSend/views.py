from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Expense, Request


class IndexView(generic.ListView):
    template_name = 'reqSend/index.html'
    context_object_name = 'latest_request_list'

    def get_queryset(self):
        '''Return the last five published requests.'''
        return Request.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Request
    template_name = 'reqSend/detail.html'

class ResultsView(generic.DetailView):
    model = Request
    template_name = 'reqSend/results.html'

def amount(appeal, request_id):
    request = get_object_or_404(Request, pk=request_id)
    try:
        selected_expense = request.expense_set.get(pk=request.POST['expense'])
    except (KeyError, Expense.DoesNotExist):
        # Redisplay the request voting form.
        return render(request, 'reqSend/detail.html', {
            'request': request,
            'error_message': "You didn't select an expense.",
        })
    else:
        selected_expense.amount += 1
        selected_expense.save()

        return HttpResponseRedirect(reverse('reqSend:results', args=(request.id,)))