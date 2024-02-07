from datetime import datetime
from json import JSONEncoder

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.defaulttags import now
from django.views.decorators.csrf import csrf_exempt

from web.models import Expense


@csrf_exempt
def submit_expense(request):
    """user submits an expense"""

    # TODO: validate data. user might be fake. token might be fake. amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(user=this_user, amount=request.POST['amount'],
                           text=request.POST['text'], date=now)

    return JsonResponse({
        'status': 'ok'
    }, endcoder=JSONEncoder)
