from django.shortcuts import render, redirect
from .models import Order
from cart.models import Cart

def checkout(request):

    items = Cart.objects.all()
    total = sum(item.total_price() for item in items)

    if request.method == "POST":

        Order.objects.create(
            customer_name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            total_amount=total
        )

        items.delete()

        return render(request, "success.html")

    return render(request, "checkout.html", {"total": total})