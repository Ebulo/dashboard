from django.shortcuts import render
from accounts.models import Merchant_Details


def landing_page(request):
    # mrd = Merchant_Details.objects.all()
    return render(request, "landing_page.html")
