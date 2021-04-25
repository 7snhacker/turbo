print("""
████████ ██    ██ ██████  ██████   ██████  
   ██    ██    ██ ██   ██ ██   ██ ██    ██ 
   ██    ██    ██ ██████  ██████  ██    ██ 
   ██    ██    ██ ██   ██ ██   ██ ██    ██ 
   ██     ██████  ██   ██ ██████   ██████  
                                                                                 
""")
print("                    by 7snhacker")
print("")
import requests
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()
user = input("Username : ")
email = input("fake email [PRESS ENTER TO SKIP] : ")
passw = input("password [PRESS ENTER TO SKIP] : ")
reghead = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '377',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'csrftoken=8eqmtlTyox2ZW9TlaXI4N1as0KkCvxBf; mid=YIIrdwALAAELzmh8avWtPbB43FDM; ig_did=D8CA9B51-358E-4367-80EF-7B8FEAC08C34; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/emailsignup/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
'x-csrftoken': '8eqmtlTyox2ZW9TlaXI4N1as0KkCvxBf',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-instagram-ajax': '2f5a8c09a5f5',
'x-requested-with': 'XMLHttpRequest'
}
while True:
    headers = {
        'authority': 'www.instagram.com',
        'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
        'x-instagram-ajax': '82a581bb9399',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'user-agent': '',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': 'rn3aR7phKDodUHWdDfCGlERA7Gmhes8X',
        'x-ig-app-id': '936619743392459',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': ''


    }
    data = {
        'username': user,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:sffdsfdsfdffrd'
    }
    url = "https://www.instagram.com/accounts/login/ajax/"
    r = requests.post(url, data=data, headers=headers).text
    if ('"user":false') in r:
        print("Avaiable ==> ",user)
        messagebox.showinfo("7snhacker", "User Avaiable")
        reg = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
        dat = {
            'email': email,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{passw}',
            'username': user,
            'first_name': 'ergegre',
            'month': '4',
            'day': '23',
            'year': '1925',
            'client_id': 'YIIrdwALAAELzmh8avWtPbB43FDM',
            'seamless_login_enabled': '1'
        }
        loginreg = requests.post(reg,data=dat , headers=reghead).text
        if ('"account_created":false') in loginreg:
            print("Registry Failed")
        elif ('"account_created":true') in loginreg:
            print("Registry Success")
            print("email : ", email)
            print("password : ", passw)
        break
    elif ('"user":true') in r:
        print("Not Avaiable ==> ",user)


