def open_account():
    print("새로운 계좌를 개설합니다.")



def deposit(balance, money): #입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance+money))
    return balance + money



def withdraw(balance, money): #출금 처리 함수
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance-money))
        return balance - money

    elif balance < money:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance

    



open_account()

balance = 1000
balance = withdraw(balance, 5000)