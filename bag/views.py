from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page """
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = request.POST.get('quantity')