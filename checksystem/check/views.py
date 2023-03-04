from django.shortcuts import render, redirect
from .models import Room, Booking, Review, AddModel
from .forms import ReviewForm

def prices(request):
    return render(request, 'prices.html')

def map1(request):
    return render(request, 'map.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        phone = request.POST['phone']
        addmodel = AddModel(name=name, phone=phone, text=text)
        addmodel.save()
        return redirect('contacts')
    return render(request, 'contacts.html')

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reviews = Review.objects.all()

        booked_rooms = Booking.objects.filter(start_date__lte=end_date, end_date__gte=start_date).values('num_rooms')
        number_of_booked_rooms = 0
        for i in booked_rooms:
            number_of_booked_rooms += i['num_rooms']
        available_rooms = 20 - number_of_booked_rooms

        return render(request, 'index.html', {'name': name, 'available_rooms': available_rooms, 'reviews': reviews})
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews': reviews})

def check_availability(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        booked_rooms = Booking.objects.filter(start_date__lte=end_date, end_date__gte=start_date).values('num_rooms')
        number_of_booked_rooms = 0
        for i in booked_rooms:
            number_of_booked_rooms += i['num_rooms']
        available_rooms = 20 - number_of_booked_rooms

        return render(request, 'availability.html', {'name': name, 'available_rooms': available_rooms})
    return render(request, 'check_availability.html')


def make_booking(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        num_rooms = request.POST['num_rooms']

        booking = Booking.objects.create(full_name=full_name, start_date=start_date, end_date=end_date,
                                         num_rooms=num_rooms)
        booking.save()

        return render(request, 'booking_confirmation.html',
                      {'full_name': full_name, 'num_rooms': num_rooms, 'start_date': start_date, 'end_date': end_date})
    return render(request, 'make_booking.html')