class unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = unit("보병", 40, 5)
soldier2 = unit("보병", 40, 5)
tank = unit("탱크", 150, 35)


# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 :"))
#     num2 = int(input("첫번째 숫자를 입력하세요 :"))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("오류 발생! 잘못된 값을 입력했습니다.")




class player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


    def attack(self,me,you,attackamount):
         self.attackamount = attackamount
         self.me = me
         self.you = you
         hpp=self.hp-attackamount

         print("{0} 캐릭터가 {1}캐릭터를 {2}의 공격력으로 공격했습니다.".format(self.me,self.you,self.attackamount))
         print("{0} 캐릭터의 체력이 {1}로 변경되었습니다.".format(self.you,hpp))

soldier1 = unit("보병", 40, 5)
soldier2 = unit("보병", 40, 5)
tank = unit("탱크", 150, 35)

tank.attack("보병","탱크",5)
