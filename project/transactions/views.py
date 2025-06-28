from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Transaction
from django.shortcuts import render

@csrf_exempt  # For simplicity; consider CSRF tokens in production
def add_transaction(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = float(data.get("amount", 0))
            description = data.get("description", "").strip()

            if amount <= 0:
                return JsonResponse({"success": False, "error": "Invalid amount"}, status=400)
            if not description:
                return JsonResponse({"success": False, "error": "Description required"}, status=400)

            Transaction.objects.create(amount=amount, description=description)
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid method"}, status=405)

def index(request):
    return render(request, 'transactions/index.html')


def transactions_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions_list.html', {'transactions': transactions})