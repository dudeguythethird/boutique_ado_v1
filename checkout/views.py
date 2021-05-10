from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get ('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IpUUMDnCLu8AdXUFDKwP3GrQv8E7CRldmjaZ7PpPOn0FWgUZVad8E2ku2yWpbMLT2qZ2SWMppa1qOIhsIaBbi4H00kmX7dRlA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
