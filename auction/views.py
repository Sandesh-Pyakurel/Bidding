import asyncio
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from .models import CustomUser, Auction, BidsToAuction
from .forms import UserSignupForm, UserLoginForm, AddAuctionForm
from .nillion.libs import store_program_nillion

def home_view(request):
    template = loader.get_template('home.html')

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

        auctions_created = Auction.objects.filter(auctioner=request.user)

        context = {
            "auction_list": auctions_created
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

