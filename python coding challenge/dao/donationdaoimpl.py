import pyodbc
from dao.donationdao import DonationDAO
from util.dbconnutil import DBConnUtil

class DonationDAOImpl(DonationDAO):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def record_cash_donation(self, donation):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into donations (donor_name, amount, donation_type, donation_date) values (?, ?, ?, ?)",
            (donation.donor_name, donation.amount, 'Cash', donation.donation_date)
        )
        self.conn.commit()
    
    def get_all_donations(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM donations")
        rows = cursor.fetchall()
        donations = []
        for row in rows:
            if row.donation_type == 'Cash':
                donation = f"[Cash] Donor: {row.donor_name}, Amount: ${row.amount}, Date: {row.donation_date}"
            elif row.donation_type == 'Item':
                donation = f"[Item] Donor: {row.donor_name}, Item: {row.item_type}"
            else:
                donation = f"[Unknown] Donor: {row.donor_name}"
            donations.append(donation)
        return donations


    def record_item_donation(self, donation):
        cursor = self.conn.cursor()
        cursor.execute(
            "insert into donations (donor_name, amount, donation_type, item_type) values (?, ?, ?, ?)",
            (donation.donor_name, donation.amount or 0, 'Item', donation.item_type)
        )
        self.conn.commit()
