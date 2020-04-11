class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

# 연락처 입력함수
def set_contact():
    name = input("name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# 연락처 출력 함수
# Contact 인스턴스를 저장하고 있는 리스트를 인자로 입력받은 후 for 문을 이용해 리스트에 저장된 인스턴스를 순회.
# 이때 각 인스턴스에서 print_info 메서드를 호출.
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제 함수
# enumerate: 열거하다 라는 뜻으로서 리스트의 원소 순서와 원소 값 2개를 동시에 반환
# 주로 for문과 함께 사용함
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

# 연락처 저장 함수
# 연락처를 txt 파일 형태로 저장
# 프로그램이 종료될 때 자동 호출
def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

# 기존 연락처 불러오기 함수
# 자동 저장된 연락처 기존 DB를 프로그램 실행 시 자동 불러오는 기능 수행
def load_contact(contact_list):
    f = open("contact_db.txt", 'rt')
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)
# 파일에 있는 모든 데이터를 읽은 후 연락처 하나 당 4줄의 데ㅔ이터가 존재하므로
# 파일에서 읽어 들인 전체 라인 수를 4로 나누어 몇 개의 데ㅔ이터가 존재하는 확인.
# 나눗셈 연산을 수행하면 num 값이 실수가 되므로, 이 값을 int 내장함수를 사용해
# 정수형으로 형태변환.
# for 문에서는 num의 개수만큼 루프를 돌면서 lines 리스트에 저장된 데ㅔ이터 읽어들여
# Contact 클래스의 인스턴스를 생성하고 생성한 인스턴스를 contact_list에 추가
# 파일로 저장된 연락처를 불러오는 것은 연락처 관리 프로그램이 실행될 때 자동 실행되어야 함.
    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

# 메뉴 입력 함수
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ =="__main__":
    run()
