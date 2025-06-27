import string
import random
import requests
import re
import os
import time
import threading
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# ---------------- CONFIG ----------------
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
SEARCH_ENGINE = "https://html.duckduckgo.com/html/?q={query}&s={start}"

FAKE_EMAIL_FILE = "fake_emails.txt"
REAL_EMAIL_FILE = "real_emails.txt"
COMBO_FILE = "combo_list.txt"
VALID_COMBO_FILE = "valid_combos.txt"

# ---------------- DATA SETS ----------------

first_names = [
    'john', 'sara', 'mark', 'emma', 'jake', 'linda', 'chris', 'anna', 'mike', 'nina',
    'paul', 'james', 'laura', 'david', 'jessica', 'kevin', 'rachel', 'brian', 'megan',
    'josh', 'karen', 'alex', 'carol', 'peter', 'susan', 'tim', 'kate', 'george', 'amanda',
    'steve', 'melissa', 'ahmed', 'mohamed', 'fatima', 'ali', 'omar', 'hassan', 'noor',
    'reem', 'khaled', 'salma', 'abdullah', 'faisal', 'layla', 'mona', 'tariq', 'yasmin',
    'huda', 'amal', 'nasser', 'waleed', 'zainab', 'hussein', 'ibrahim', 'samir', 'jamal',
    'dina', 'nawal', 'sami', 'ghada', 'yousef', 'saeed', 'nour', 'mariam', 'maha', 'rawan',
    'bassam', 'samira', 'adel', 'nabil', 'karim', 'eman', 'rabia', 'fadi', 'farah', 'hiba',
    'zaki', 'khalil', 'lina', 'soha', 'rashid', 'jawad', 'liam', 'noah', 'olivia', 'ava',
    'isabella', 'sophia', 'mia', 'charlotte', 'amelia', 'harper', 'li', 'wei', 'ming', 'jun',
    'mei', 'yuki', 'hiro', 'takashi', 'an', 'bao', 'raj', 'arjun', 'neha', 'fatimah', 'abdul',
    'saleh', 'zara', 'omarion', 'kai', 'elan', 'nayla', 'samara', 'talia'
]

last_names = [
    'doe', 'smith', 'brown', 'white', 'king', 'johnson', 'lee', 'clark', 'hall', 'wright',
    'ali', 'hassan', 'ahmed', 'khan', 'mohammed', 'faris', 'mansour', 'hamdan', 'abbas',
    'fahad', 'sultan', 'rashid', 'matar', 'sabah', 'soud', 'nasr', 'hilal', 'kamel', 'bakr',
    'fahmy', 'zaki', 'nasser', 'taha', 'mahmoud', 'morsi', 'samir', 'younes', 'sharif',
    'darwish', 'adel', 'hisham', 'kareem', 'ismail', 'salem', 'barakat', 'omar', 'khoury',
    'zidan', 'selim', 'fouad', 'jamal', 'anderson', 'thomas', 'martin', 'garcia', 'rodriguez',
    'wilson', 'moore', 'taylor', 'jackson', 'whitehead', 'reed', 'collins', 'murphy',
    'cooper', 'kelly', 'ward', 'morgan', 'harris', 'ross', 'jenkins', 'bell', 'richardson',
    'ramos', 'singh', 'patel', 'wrightson', 'hoffman', 'bauer', 'schmidt', 'muller', 'keller',
    'herrera', 'gomez', 'fernandez', 'ruiz', 'vazquez', 'mendez'
]

adjectives = [
    'fast', 'cool', 'hot', 'red', 'blue', 'dark', 'happy', 'sad', 'wild', 'quiet',
    'crazy', 'brave', 'smart', 'lazy', 'noisy', 'strong', 'gentle', 'clever', 'loyal', 'fearless',
    'fierce', 'bold', 'mighty', 'sly', 'swift', 'silent', 'proud', 'noble', 'keen', 'bold'
]

nouns = [
    'tiger', 'lion', 'eagle', 'wolf', 'shark', 'dragon', 'hawk', 'fox', 'bear', 'snake',
    'panther', 'falcon', 'rhino', 'cobra', 'cheetah', 'leopard', 'wolfie', 'hyena', 'jackal', 'lynx',
    'viper', 'bull', 'stallion', 'griffin', 'phoenix', 'otter', 'raven', 'bison', 'orca', 'python',
    'cougar', 'jackrabbit', 'mink', 'heron', 'caracal', 'coyote', 'dingo', 'fennec'
]

separators = ['', '.', '_', '-']

password_charsets = {
    "simple": string.ascii_lowercase + string.digits,
    "strong": string.ascii_letters + string.digits + "!@#$%^&*()-_=+",
    "letters": string.ascii_letters,
}

# ---------------- STYLES ----------------
ALL_STYLES = list(range(1, 31))  # Expanded to 30 styles!

STYLE_EXPLANATIONS = {
    1: "Random letters and digits (8 chars)",
    2: "First name + Last name",
    3: "First name + random 2-4 digit number",
    4: "First name.dot.Last name",
    5: "Adjective + Noun + 3 digit number",
    6: "Noun + separator + 3 digit number",
    7: "First name + separator + Last name + 3 digit number",
    8: "Adjective + First name + 3 digit number",
    9: "First name + 2-digit number",
    10: "Adjective + Noun + 3-digit number (zero padded)",
    11: "Random adjective + separator + noun",
    12: "Noun + year (1970-2025)",
    13: "First initial + Last name + 2-digit number",
    14: "First name + Last initial + 2-digit number",
    15: "Custom base name only",
    16: "Custom base name + random digits",
    17: "Custom base name + separator + random digits",
    18: "Custom base name + adjective + number",
    19: "Custom base name + noun + number",
    20: "Custom base name + separator + adjective + number",
    21: "First name + noun + random digits",
    22: "Adjective + custom base name + digits",
    23: "Last name + random digits",
    24: "Noun + separator + custom base name",
    25: "Random letters + custom base name + digits",
    26: "Custom base name + letters + digits",
    27: "First name + separator + custom base name",
    28: "Custom base name + separator + last name",
    29: "Custom base name + noun + separator + digits",
    30: "Letters + digits (10 chars random)",
}

# ---------------- UTILITIES ----------------

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_line(title):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)

# ---------------- GENERATE USERNAME ----------------

def generate_username(style, custom_name=None):
    num = str(random.randint(0, 9999))
    num_2d = str(random.randint(10, 99))
    num_3d = str(random.randint(0, 999)).zfill(3)
    sep = random.choice(separators)
    
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    cbase = custom_name.lower() if custom_name else None
    
    if style == 1:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    elif style == 2:
        return fn + ln
    elif style == 3:
        return fn + str(random.randint(10, 9999))
    elif style == 4:
        return fn + '.' + ln
    elif style == 5:
        return adj + noun + num_3d
    elif style == 6:
        return noun + sep + num_3d
    elif style == 7:
        return fn + sep + ln + num_3d
    elif style == 8:
        return adj + fn + num_3d
    elif style == 9:
        return fn + num_2d
    elif style == 10:
        return adj + noun + num_3d
    elif style == 11:
        return adj + sep + noun
    elif style == 12:
        return noun + str(random.randint(1970, 2025))
    elif style == 13:
        return fn[0] + ln + num_2d
    elif style == 14:
        return fn + ln[0] + num_2d
    elif style == 15:
        return cbase or fn
    elif style == 16:
        return (cbase or fn) + num
    elif style == 17:
        return (cbase or fn) + sep + num
    elif style == 18:
        return (cbase or fn) + adj + num_2d
    elif style == 19:
        return (cbase or fn) + noun + num_2d
    elif style == 20:
        return (cbase or fn) + sep + adj + num_2d
    elif style == 21:
        return fn + noun + num_2d
    elif style == 22:
        return adj + (cbase or fn) + num_2d
    elif style == 23:
        return ln + num_3d
    elif style == 24:
        return noun + sep + (cbase or fn)
    elif style == 25:
        return ''.join(random.choices(string.ascii_lowercase, k=3)) + (cbase or fn) + num_2d
    elif style == 26:
        return (cbase or fn) + ''.join(random.choices(string.ascii_letters, k=2)) + num_2d
    elif style == 27:
        return fn + sep + (cbase or fn)
    elif style == 28:
        return (cbase or fn) + sep + ln
    elif style == 29:
        return (cbase or fn) + noun + sep + num_2d
    elif style == 30:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    else:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# ---------------- PASSWORD GENERATION ----------------

def generate_password(style='strong'):
    length = random.randint(8, 16)
    charset = password_charsets.get(style, password_charsets['strong'])
    return ''.join(random.choice(charset) for _ in range(length))

# ---------------- GENERATE FAKE EMAILS ----------------

def generate_fake_emails(domains, count, styles, custom_name=None):
    seen = set()
    total = 0
    with open(FAKE_EMAIL_FILE, "w", encoding="utf-8") as f:
        while total < count:
            style = random.choice(styles)
            domain = random.choice(domains)
            username = generate_username(style, custom_name)
            email = f"{username}@{domain}"
            if email not in seen:
                seen.add(email)
                f.write(email + "\n")
                total += 1
                print(f"[{total}/{count}] Generated: {email}")
    print(f"\n[✔] {count} fake emails saved to {FAKE_EMAIL_FILE}")

# ---------------- GENERATE FAKE COMBOS ----------------

def generate_fake_combos(domains, count, styles, custom_name=None, pass_style='strong'):
    seen = set()
    total = 0
    with open(COMBO_FILE, "w", encoding="utf-8") as f:
        while total < count:
            style = random.choice(styles)
            domain = random.choice(domains)
            username = generate_username(style, custom_name)
            password = generate_password(pass_style)
            combo = f"{username}@{domain}:{password}"
            if combo not in seen:
                seen.add(combo)
                f.write(combo + "\n")
                total += 1
                print(f"[{total}/{count}] Generated combo: {combo}")
    print(f"\n[✔] {count} fake combos saved to {COMBO_FILE}")

# ---------------- EMAIL EXTRACTION ----------------

def extract_emails_from_text(text, domain=None):
    pattern = rf"[a-zA-Z0-9.%+-]+@{re.escape(domain)}" if domain else r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def extract_combos_from_text(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[^\s]+"
    return re.findall(pattern, text)

# ---------------- SCRAPE REAL EMAILS ----------------

def scrape_real_emails(domain, max_pages):
    session = requests.Session()
    found_emails = set()
    print(f"\n[✓] Starting real email search for: {domain}")
    for page in range(max_pages):
        print(f"[*] Searching page {page+1}/{max_pages}...")
        query = f"@{domain}"
        url = SEARCH_ENGINE.format(query=quote_plus(query), start=page * 30)
        try:
            res = session.get(url, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(res.text, "html.parser")
            links = [a['href'] for a in soup.find_all("a", href=True)]
            for link in links:
                try:
                    sub_res = session.get(link, headers=HEADERS, timeout=10)
                    emails = extract_emails_from_text(sub_res.text, domain)
                    for email in emails:
                        if email not in found_emails:
                            print(f"[✓] Found: {email}")
                            found_emails.add(email)
                except:
                    continue
        except Exception as e:
            print(f"[!] Error on page {page+1}: {e}")
        time.sleep(1.5)
    with open(REAL_EMAIL_FILE, "w", encoding="utf-8") as f:
        for email in sorted(found_emails):
            f.write(email + "\n")
    print(f"\n[✔] {len(found_emails)} real emails saved to {REAL_EMAIL_FILE}")

# ---------------- SCRAPE COMBOS ----------------

def scrape_combos(max_pages):
    session = requests.Session()
    found_combos = set()
    print(f"\n[✓] Starting combo list extraction (email:pass format)")
    for page in range(max_pages):
        print(f"[*] Searching page {page+1}/{max_pages}...")
        query = "intext:@gmail.com filetype:txt"
        url = SEARCH_ENGINE.format(query=quote_plus(query), start=page * 30)
        try:
            res = session.get(url, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(res.text, "html.parser")
            links = [a['href'] for a in soup.find_all("a", href=True)]
            for link in links:
                try:
                    sub_res = session.get(link, headers=HEADERS, timeout=10)
                    combos = extract_combos_from_text(sub_res.text)
                    for combo in combos:
                        if combo not in found_combos:
                            print(f"[✓] Found combo: {combo}")
                            found_combos.add(combo)
                except:
                    continue
        except Exception as e:
            print(f"[!] Error on page {page+1}: {e}")
        time.sleep(1.5)
    with open(COMBO_FILE, "w", encoding="utf-8") as f:
        for combo in sorted(found_combos):
            f.write(combo + "\n")
    print(f"\n[✔] {len(found_combos)} combos saved to {COMBO_FILE}")

# ---------------- LOAD PROXIES ----------------

def load_proxies(proxy_file):
    proxies = []
    try:
        with open(proxy_file, "r", encoding="utf-8") as f:
            for line in f:
                proxy = line.strip()
                if proxy:
                    proxies.append(proxy)
    except Exception as e:
        print(f"Error loading proxies: {e}")
    return proxies

def choose_proxy(proxies, mode, counter):
    if not proxies:
        return None
    if mode == 'random':
        return random.choice(proxies)
    elif mode == 'round':
        proxy = proxies[counter % len(proxies)]
        return proxy
    else:
        return None

# ---------------- COMBO CHECKER SIMULATION ----------------
# Replace this with real API check or IMAP/SMTP auth

def check_combo_validity(email, password, proxy=None):
    # Simulated check: randomly return True (valid) 20% of time
    time.sleep(0.1)
    return random.random() < 0.2

# ---------------- CHECK COMBOS ----------------

def check_combos(combo_file, proxy_file=None, proxy_mode='random', threads=10):
    combos = []
    with open(combo_file, "r", encoding="utf-8") as f:
        combos = [line.strip() for line in f if line.strip()]
    proxies = load_proxies(proxy_file) if proxy_file else []
    valid_combos = []
    total = len(combos)
    lock = threading.Lock()
    counter = 0

    def worker():
        nonlocal counter
        while True:
            with lock:
                if counter >= total:
                    return
                combo = combos[counter]
                counter += 1
            if ':' not in combo:
                continue
            email, password = combo.split(":", 1)
            proxy = choose_proxy(proxies, proxy_mode, counter)
            print(f"Checking: {email}:{password} via proxy: {proxy}")
            if check_combo_validity(email, password, proxy):
                print(f"[✔] Valid combo: {email}:{password}")
                valid_combos.append(combo)

    threads_list = []
    for _ in range(min(threads, total)):
        t = threading.Thread(target=worker)
        t.start()
        threads_list.append(t)
    for t in threads_list:
        t.join()

    with open(VALID_COMBO_FILE, "w", encoding="utf-8") as f:
        for combo in valid_combos:
            f.write(combo + "\n")
    print(f"\n[✔] {len(valid_combos)} valid combos saved to {VALID_COMBO_FILE}")

# ---------------- MAIN CLI ----------------

def main():
    clear_console()
    print_line("🔥 Ultimate Email & Combo Toolkit - CLI Version 🔥")

    while True:
        print("\nSelect Mode:")
        print("1. Generate Fake Emails")
        print("2. Generate Fake Combos (email:pass)")
        print("3. Extract Real Emails from Web")
        print("4. Extract Email:Password Combos from Web")
        print("5. Check Combos Validity (Simulated)")
        print("6. Exit")

        choice = input("\nEnter your choice [1-6]: ").strip()
        if choice == '1':
            domains = input("Enter domain(s) separated by commas (e.g. gmail.com,yahoo.com): ").strip().lower().split(",")
            count = int(input("Number of fake emails to generate: ").strip())
            print("\nAvailable username styles:")
            for i in ALL_STYLES:
                print(f"{i}. {STYLE_EXPLANATIONS.get(i, f'Style {i}')}")
            styles_input = input("Choose styles separated by commas or 'all' for all styles: ").strip()
            if styles_input.lower() == 'all':
                styles = ALL_STYLES
            else:
                styles = [int(s) for s in styles_input.split(",") if s.strip().isdigit() and int(s) in ALL_STYLES]
                if not styles:
                    styles = [1]
            custom_name = input("Enter a custom base name to focus on (or leave empty): ").strip() or None
            generate_fake_emails(domains, count, styles, custom_name)

        elif choice == '2':
            domains = input("Enter domain(s) separated by commas (e.g. gmail.com,yahoo.com): ").strip().lower().split(",")
            count = int(input("Number of fake combos to generate: ").strip())
            print("\nAvailable username styles:")
            for i in ALL_STYLES:
                print(f"{i}. {STYLE_EXPLANATIONS.get(i, f'Style {i}')}")
            styles_input = input("Choose styles separated by commas or 'all' for all styles: ").strip()
            if styles_input.lower() == 'all':
                styles = ALL_STYLES
            else:
                styles = [int(s) for s in styles_input.split(",") if s.strip().isdigit() and int(s) in ALL_STYLES]
                if not styles:
                    styles = [1]
            custom_name = input("Enter a custom base name to focus on (or leave empty): ").strip() or None
            print("Password styles: simple, strong, letters")
            pass_style = input("Choose password style (default: strong): ").strip().lower()
            if pass_style not in password_charsets:
                pass_style = 'strong'
            generate_fake_combos(domains, count, styles, custom_name, pass_style)

        elif choice == '3':
            domain = input("Enter domain to scrape real emails from (e.g. gmail.com): ").strip().lower()
            pages = int(input("Number of search pages to scan: ").strip())
            scrape_real_emails(domain, pages)

        elif choice == '4':
            pages = int(input("Number of search pages to scan for combos: ").strip())
            scrape_combos(pages)

        elif choice == '5':
            combo_file = input("Enter path to combo file (email:pass): ").strip()
            proxy_file = input("Enter proxy file path (optional): ").strip() or None
            proxy_mode = input("Proxy mode [random/round/none]: ").strip().lower()
            if proxy_mode not in ['random', 'round', 'none']:
                proxy_mode = 'random'
            threads = input("Number of threads (default 10): ").strip()
            threads = int(threads) if threads.isdigit() else 10
            check_combos(combo_file, proxy_file, proxy_mode, threads)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

#########################################################

#import string
#import random
#letters = string.ascii_lowercase
#print("yahoo"'\n'
#      "gmail"'\n'
#      "aol"'\n'
#      "write any domail")
#email = input("domain : ")
#m = int(input("How many emails: "))
#done = 0
#li = 0
#lst = open("email.txt", "w")
#ranges = int(input("email characters range : "))
#while li == 0:
#    lst.write( ''.join(random.choice(letters) for i in range(ranges))+f'@{email}.com'+'\n')
#    done += 1
#    print(done)
#    if done == m:
#        li = 1
#        while True:
#            print("Done (:")
#            print("Click Ctrl C to Exit")
#            input("")
