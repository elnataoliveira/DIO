from controller.checkin_account_controller import Checking_Account_Controller
from controller.client_controller import Client_Controller
from view.menu import Menu
from db.database import Database

def main():
    db = Database()
    db.create_tables()
    cur = db.cursor

    menu = Menu()
    menu.interface(Checking_Account_Controller(), Client_Controller())


if __name__ == '__main__':
    main()
