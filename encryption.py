def str_to_ascii(string:str):
    '''FONKSİYON ISLEVİ
    Alinan metni cümlelere böler, bu cümlelerde gecen her bir karakteri sirasiyla ascii karsiligini alir
    ve ascii_list icine ekler ve bu listeyi return eder.
    '''
    ascii_list = [ord(char) for char in string]
    return ascii_list

def encryption(ascii_list:list):
    encrypted_list = [f"{code:07}" for code in ascii_list ]
    return encrypted_list

def file_save(encrypt_ascii_list: list, file_name: str):
    with open(file_name, 'w') as file:
        for code in encrypt_ascii_list:
            file.write(str(code))
    return  None

def main():
    string = input("Mesaj Girin: ")
    ascii_list = str_to_ascii(string)
    encrypted_list = encryption(ascii_list)
    file_save(encrypted_list, 'encrypted_list.txt')

if __name__ == '__main__':
    main()