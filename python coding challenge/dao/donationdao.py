from abc import ABC, abstractmethod
from entity.cashdonation import CashDonation
from entity.itemdonation import ItemDonation

class DonationDAO(ABC):
    @abstractmethod
    def record_cash_donation(self, donation: CashDonation):
        pass

    @abstractmethod
    def record_item_donation(self, donation: ItemDonation):
        pass
