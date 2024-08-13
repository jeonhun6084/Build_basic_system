class Account:
    def __init__(self, account_id, customer_name, balance):
        self.account_id = account_id
        self.customer_name = customer_name
        self.balance = balance

    # def get_account_id():
    #     return
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount > 0:
            print("출금완료")
            self.balance -= withdraw_amount
        else:
            print("잔액이 부족합니다.")

    def show_account_information(self):
        print(f'계좌ID:{self.account_id}')
        print(f'이    름:{self.customer_name}')
        print(f'잔    액:{self.balance}')
   


def show_menu():
   print(' -----Menu------')
   print(' 1. 계좌개설')
   print(' 2. 입    금')
   print(' 3. 출    금')
   print(' 4. 계좌정보 전체 출력')
   print(' 5. 프로그램 종료')

def menu_input():
    return int(input(''))

def make_account(account_list, num_of_accounts):
    print('[계좌 개설]')
    account_id = input('계좌ID:')
    customer_name = input('이  름:')
    balance = int(input('입금액:'))
    user = Account(account_id, customer_name, balance)
    account_list.append(user)
    num_of_accounts += 1

def deposit_money(account_list):
    print('[입    금]')
    account_id = input('계좌ID:')
    deposit_amount = int(input('입금액:'))
    for user in account_list:
        if account_id == user.account_id:
            user.deposit(deposit_amount)
            print("입금완료")
        else:
            print("유효하지 않는 ID입니다")

def withdraw_money(account_list):
    print('[출    금]')
    account_id = input('계좌ID:')
    withdraw_amount = int(input('출금액:'))
    for user in account_list:
        if account_id == user.account_id:
            user.withdraw(withdraw_amount)
        else:
            print("유효하지 않는 ID입니다")

def show_all_account_information(account_list):
    # 현재 저장된 모든 계좌의 정보 출력
    for user in account_list:
        user.show_account_information()


account_list = []
num_of_accounts = 0

def main():

    """Main function to run the banking system."""
    while True:
        show_menu()
        choice = menu_input()
        print()

        if choice == 1:
            make_account(account_list, num_of_accounts)
        elif choice == 2:
            deposit_money(account_list)
        elif choice == 3:
            withdraw_money(account_list)
        elif choice == 4:
            show_all_account_information(account_list)
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name__ == "__main__":
    main()