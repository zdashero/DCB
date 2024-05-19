import requests

def main():
    print("Double Counter Bypass by zdashero on github and discord")
    code = ""

    while not code:
        code = input("[+] Please, insert a valid Double Counter verification link / code here: ").strip()

        if code.startswith("https://"):
            code = code[len("https://"):]
        if code.startswith("http://"):
            code = code[len("http://"):]
        if code.startswith("www."):
            code = code[len("www."):]

        if code.startswith("verify.doublecounter.gg/v/"):
            code = code[len("verify.doublecounter.gg/v/"):]

        if len(code) < 3:
            print("[+] Inserted link or code is not valid.")
            code = ""

    url = f"https://verify.doublecounter.gg/v/{code}"

    headers = {
        "Host": "verify.doublecounter.gg",
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("[+] Successfully Bypassed Double Counter.")
    else:
        print(f"[+] Failed to verify. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
