'''
С клавиатуры вводят пароль. 
Проверить валидность ввода пароля. 
Валидный пароль должен содержать в себе хотя бы 1 букву в верхнем регистре, 
хотя бы 1 букву в нижнем регистре, 
хотя бы 1 цифру и должен быть длиной не менее 8 символов.

Пример
ввод - HelloMyNameIs88
вывод - Пароль валиден

if len(password) > 8 :
        print('да')
    else: 
        print('нет')


'''

def validate_password(password):
    has_upper_letter = False
    has_lower_letter = False
    has_number = False
    for letter in password:
            if letter.isupper():
                has_upper_letter = True
            if letter.islower():
                has_lower_letter = True
            if letter.isdigit():
                has_number = True 
    if has_upper_letter and has_lower_letter and has_number and len(password) > 8:
        return True
    else:
        return False

def test_validate_password():
    password_without_digit = 'Burundukk'
    password_without_lower_letter = 'DIMA19966'
    password_without_upper_letter = 'guz200111'
    password_without_correct_length = 'Ab123'
    password_correct = 'HelloMyNameIs88'
    if not validate_password(password_without_digit):
        print('ok')
    if not validate_password(password_without_lower_letter ):
        print('ok')
    if not validate_password(password_without_upper_letter):
        print('ok')
    if  not validate_password(password_without_digit):
        print('ok')     
    if  validate_password(password_correct):
        print('ok')        
        
test_validate_password()
