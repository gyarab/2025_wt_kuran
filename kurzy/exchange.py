import httpx
import sys
from colorama import Fore, Style, init

init(autoreset=True)

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

lines = res.text.splitlines()
header = lines[0].split(" #")[0]

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

parts = line_euro.split('|')
rate = float(parts[-1].replace(',', '.'))

print(Fore.CYAN + "=" * 30)
print(Fore.YELLOW + f"Kurzy ČNB pro den: {header}")
print(Fore.CYAN + "=" * 30)
print(f"Aktuální kurz: 1 EUR = {rate} CZK")
print("-" * 30)

print("Vyberte směr převodu:")
print("1: EUR -> CZK")
print("2: CZK -> EUR")

volba = input(Fore.BLUE + "Vaše volba: ")

try:
    if volba == "1":
        castka = float(input("Zadejte částku v EUR: ").replace(',', '.'))
        vysledek = castka * rate
        print(Fore.GREEN + f"{castka} EUR = {vysledek:.2f} CZK")
    elif volba == "2":
        castka = float(input("Zadejte částku v CZK: ").replace(',', '.'))
        vysledek = castka / rate
        print(Fore.GREEN + f"{castka} CZK = {vysledek:.2f} EUR")
    else:
        print(Fore.RED + "Neplatný vstup. Zvolte 1 nebo 2.")
except ValueError:
    print(Fore.RED + "Error: Neplatná číselná hodnota.")

print(Fore.CYAN + "=" * 30)