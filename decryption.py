def decryption_file(file_name:str):
    '''
    Docstring for decryption_file
    
    :param file_name: Description
    :type file_name: str

    Şifreli dosyayi okur ve string olarak döndürür
    '''
    with open(file_name, 'r') as file:
        encrypted_string = file.read()
    return encrypted_string

def open_code(encrypted_string_list:str, code_order:int):
    '''
    Docstring for open_code
    
    :param encrypted_string_list: Description
    :type encrypted_string_list: str
    :param code_order: Description
    :type code_order: int

    Şifreli satiri alir her karakter kodunu bulur ve bir listeye atar
    '''
    string_code_list = [
        encrypted_string_list[i:i+code_order] for i in range(0, len(encrypted_string_list), code_order)
    ]
    return string_code_list

def decryption_code(string_code_list:list):
    full_string = "".join([chr(int(code)) for code in string_code_list])
    return full_string

def main():
    file_name = input("Şifreli Dosyanın İsmi: ")
    encrypted_string= decryption_file(file_name)
    string_code_list = open_code(encrypted_string, 7)
    full_string = decryption_code(string_code_list)
    print(full_string)

if __name__ == '__main__':
    main()
    print(str.join.__doc__)