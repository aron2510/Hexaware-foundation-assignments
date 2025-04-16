from entity.donation import Donation

class CashDonation(Donation):
    def __init__(self, donor_name, amount, donation_date):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date

    def record_donation(self):
        print(f"Cash donation recorded from {self.donor_name} of amount ${self.amount} on {self.donation_date}")
