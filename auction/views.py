import asyncio
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.utils import timezone
from django.db.models import Q

from .models import CustomUser, Auction, BidsToAuction
from .forms import UserSignupForm, UserLoginForm, AddAuctionForm
from .nillion.libs import store_program_nillion

def home_view(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render(request=request))

def auction_view(request):
    template = loader.get_template('auctions.html')

    return HttpResponse(template.render(request=request))

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.is_auctioner:
                return redirect('auctioner')
            else:
                return redirect('bidder')
    else:
        form = UserSignupForm()
    template = loader.get_template('signup_page.html')

    return HttpResponse(template.render({'form': form}, request=request))


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                if user.is_auctioner:
                    return redirect('auctioner')
                else:
                    return redirect('bidder')
    else:
        form = UserLoginForm()
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render({'form': form}, request=request))


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def auctioner_view(request):
    if request.user.is_auctioner:
        template = loader.get_template('auctioner_page.html')

        filter_type = request.GET.get('filter')
        search_query = request.GET.get('search')
        auctions_created = Auction.objects.filter(auctioner=request.user)

        if filter_type == 'completed':
            auctions_created = auctions_created.filter(ending_date__lt=timezone.now())
        elif filter_type == 'ongoing':
            auctions_created = auctions_created.filter(ending_date__gt=timezone.now(), created_date__lt=timezone.now(), is_closed=False)
        elif filter_type == 'upcoming':
            auctions_created = auctions_created.filter(created_date__gt=timezone.now())

        if search_query:
            auctions_created = auctions_created.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )

        context = {
            "auction_list": auctions_created,
            "search_query": search_query,
            "filter_type": filter_type,
        }

        return HttpResponse(template.render(context=context, request=request))


@login_required
def add_auction_view(request):
    if request.user.is_auctioner:
        if request.method == 'POST':
            form = AddAuctionForm(request.POST, request.FILES)
            if form.is_valid():
                auction = form.save(commit=False)
                auction.auctioner = request.user
                program_id = asyncio.run(store_program_nillion.store_program_in_nillion())
                auction.program_id = program_id
                auction.save()

                return redirect('auctioner')

            else:
                print(form.errors)
        else:
            form = AddAuctionForm()
        template = loader.get_template('add_auction_page.html')
        return HttpResponse(template.render(context={'form':form}, request=request))

