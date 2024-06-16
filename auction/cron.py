from django_cron import CronJobBase, Schedule
from django.utils import timezone

from .models import Auction

class CheckAuctionsCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'auction.check_auctions_cron_job'

    def do(self):
        now = timezone.now()
        auctions_to_close = Auction.objects.filter(ending_date__lte=now, is_closed=False)

        for auction in auctions_to_close:
            auction.close_auction()