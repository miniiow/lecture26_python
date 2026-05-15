class Member:
    def __init__(self, user_no, id, pw, name, phone, address):
        self.__user_no = user_no
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__phone = phone
        self.__address = address

    def __str__(self):
        return f'\n회원번호: {self.__user_no}\n아이디: {self.__id}\t비밀번호: {self.__pw}\n회원명: {self.__name}\n전화번호: {self.__phone}\n주소: {self.__address}\n-----------------------------------------'
    
    def update_member(self, name, pw, phone, address):
        self.__name = name
        self.__pw = pw
        self.__phone = phone
        self.__address = address

    def get_user_no(self):
        return self.__user_no
    
class MemberService:
    def __init__(self):
        self.__member_list = []

    # 회원가입
    def create_member(self, user_no, id, pw, name, phone, address):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                return False
        member = Member(user_no, id, pw, name, phone, address)
        self.__member_list.append(member)
        return True
    # 회원목록
    def list_member(self):
        return self.__member_list
    # 회원상세정보
    def info_member(self, user_no):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                print(member)
                return True
        return False
    # 회원정보수정
    def update_member(self, user_no, name, pw, phone, address):
        for member in self.__member_list :
            if member.get_user_no() == user_no:
                member.update_member(name, pw, phone, address)
                return True
        return False
    # 회원탈퇴
    def delete_member(self, user_no):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                self.__member_list.remove(member)
                return True
        return False
    # 회원리스트 여부확인
    def is_member_there(self):
        if len(self.__member_list) > 0:
            return True
        return False
    
def select_menu():
    print('===================================================================================')
    print(' 1.회원가입 | 2.회원목록 | 3.회원상세정보 | 4.회원정보수정 | 5.회원탈퇴 | 0.종료')
    print('==================================================================================')
    menu = int(input('>> 메뉴선택 : '))
    return menu

memservice = MemberService()

print()
print('=============== 회원관리 ===============')
while True:  
    try:
        menu = select_menu()
    except ValueError:
        print('[오류] 정수로 입력해주세요.')
    else:
        if menu == 0 : break
        elif menu == 1:     #회원가입
            # 회원번호, 아이디, 비밀번호, 이름, 전화번호, 주소입력받아 회원가입 진행
            user_no = int(input('> 회원번호 : '))
            id = input('> 아이디 : ')
            pw = input('> 비밀번호 : ')
            name = input('> 이름 : ')
            phone = input('> 전화번호 : ')
            address = input('> 주소 : ')
            if memservice.create_member(user_no, id, pw, name, phone, address):
                print('결과 : 회원가입이 성공했습니다. 환영합니다 !!')
            else:
                print('결과 : 중복된 회원번호입니다.')
            
        elif menu == 2:     #회원목록 조회
            if memservice.is_member_there():
                member_list = memservice.list_member()
                for member in member_list:
                    print(member)
            else:
                print('등록된 회원이 없습니다.')

        elif menu == 3:     #회원상세정보 조회
            if memservice.is_member_there():
                try:
                    user_no = int(input('> 회원번호 : '))
                except ValueError:
                    print('[오류] 정수로 입력해주세요.')
                else:
                    if memservice.info_member(user_no):
                        print('\n결과 : 회원상세정보 조회완료\n')
                    else:
                        print('결과 : 회원정보가 없습니다.')
            else:
                print('등록된 회원이 없습니다.')

        elif menu == 4:     #회원정보수정
            if memservice.is_member_there():
                try:           
                    user_no = int(input('> 수정할 회원번호 : '))
                except ValueError:
                    print('[오류] 정수로 입력해주세요.')
                else:
                    name = input('> 새 이름 : ')
                    pw = input('> 새 비밀번호 : ')
                    phone = input('> 새 전화번호 : ')
                    address = input('> 새 주소 : ')
                    if memservice.update_member(user_no, name, pw, phone, address):
                        print('\n결과 : 회원정보 수정완료\n')
                    else:
                        print('\n결과 : 수정할 회원정보가 없습니다.')
            else:
                print('등록된 회원이 없습니다.')     

        elif menu == 5:     #회원탈퇴
            if memservice.is_member_there():
                try:
                    user_no = int(input('> 탈퇴할 회원번호 : '))
                except ValueError:
                    print('[오류] 정수로 입력해주세요.')
                else:
                    if memservice.delete_member(user_no):
                        print('\n결과: 회원탈퇴 완료')
                    else:
                        print('해당 회원번호가 존재하지 않습니다.')
            else:
                print('등록된 회원이 없습니다.')
        else:
            print('\n[오류] 메뉴에 없는 숫자를 입력하셨습니다.\n다시 입력해주세요')
            continue
        

print('\n========== 이용해 주셔서 감사합니다. ==========\n')