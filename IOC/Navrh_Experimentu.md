# Návrh experimentů

Tato sekce popisuje experimentální design pro hodnocení schopností velkých jazykových modelů (LLM) v různých oblastech.

## Společná kritéria hodnocení pro všechny experimenty:

Pro každou odpověď modelu budeme hodnotit následující metriky:

1.  **Správnost odpovědi:** Je odpověď fakticky správná? (Ano / Ne / Částečně)
2.  **Čas do vygenerování odpovědi:** Doba, za jak dlouho model odpověď vygeneruje. (v sekundách)
3.  **Přítomnost "halucinací":** Obsahuje odpověď smyšlené nebo nepravdivé informace prezentované jako fakta? (Ano / Ne)
4.  **Uvedení zdrojů:** Odkazoval model na externí zdroje informací? (Ano / Ne)
5.  **Správné použití českého jazyka:** Je odpověď stylisticky a gramaticky správná, přirozená a srozumitelná v českém jazyce? (špatné, dobré, výborné)

## Typy experimentů:

### 1. Vědomostní otázky

Cílem je ověřit faktickou přesnost a rozsah znalostí modelů.

**Sada otázek:**

1.  **Historie:** Ve kterém roce začala a skončila druhá světová válka?
2.  **Věda (Fyzika):** Jaká je rychlost světla ve vakuu (uveďte v km/s)?
3.  **Věda (Biologie):** Co je to fotosyntéza? Popište stručně proces.
4.  **Geografie:** Která řeka je nejdelší na světě?
5.  **Literatura:** Kdo napsal román "1984"?
6.  **Umění:** Kdo je autorem sochy Davida?
7.  **Technologie:** Co znamená zkratka "HTTP"?
8.  **Současné dění:** Která soukromá společnost jako první dopravila astronauty na Mezinárodní vesmírnou stanici (ISS)?
9.  **Česká historie:** Kdy byla založena Karlova univerzita v Praze?
10. **Mytologie:** Kdo byl v řecké mytologii bohem moře?

<br>

### 2. Logické problémy

Cílem je ověřit schopnost modelů uvažovat, řešit problémy a vyvozovat závěry z daných informací, včetně rozpoznávání logických klamů.

**Sada úloh:**

**2.1. Hádanky:**

1.  > Jsi v místnosti se třemi vypínači a v sousední místnosti jsou tři žárovky. Každý vypínač ovládá jednu žárovku. Do místnosti se žárovkami smíš vejít pouze jednou. Jak zjistíš, který vypínač patří ke které žárovce?
2.  > Co má oči, ale nevidí?
3.  > Když mě máš, chceš mě sdílet. Když mě sdílíš, nemáš mě. Co jsem?

**Správné odpovědi k hádankám:**

1.  > **Tři vypínače a žárovky:** Zapněte první vypínač a nechte ho chvíli zapnutý. Pak ho vypněte. Zapněte druhý vypínač. Jděte do místnosti se žárovkami. Jedna žárovka bude svítit (patří k druhému vypínači). Jedna žárovka bude zhasnutá, ale teplá (patří k prvnímu vypínači). Jedna žárovka bude zhasnutá a studená (patří ke třetímu vypínači).
2.  > **Co má oči, ale nevidí?** Brambora (nebo jehla, bouře, atd. – nejčastější odpověď je brambora).
3.  > **Když mě máš, chceš mě sdílet...** Tajemství.

**2.2. Slovní úlohy:**

4.  > Na stole leží tři krabice. Jedna obsahuje pouze jablka, jedna pouze pomeranče a jedna směs jablek a pomerančů. Všechny krabice jsou špatně označené. Můžeš si vzít pouze jeden kus ovoce z jedné libovolné krabice (bez dívání se dovnitř). Jak zjistíš, co je v které krabici?
5.  > Lékař vám dá tři pilulky a řekne vám, abyste si vzali jednu každou půlhodinu. Jak dlouho vám bude trvat, než si vezmete všechny pilulky?
6.  > Muž se podívá na portrét a řekne: "Bratry a sestry nemám, ale otec tohoto muže je synem mého otce." Na koho se muž na portrétu dívá?

**Správné odpovědi ke slovním úlohám:**

4.  > **Tři krabice s ovocem:** Vezměte ovoce z krabice označené "Jablka a Pomeranče". Pokud vytáhnete jablko, pak tato krabice je "Jablka". Protože všechny krabice jsou špatně označené, krabice označená "Pomeranče" musí být "Směs" a krabice označená "Jablka" musí být "Pomeranče". (A naopak, pokud vytáhnete pomeranč).
5.  > **Tři pilulky:** Jedna hodina. (Vezmete první pilulku v čase 0, druhou za 30 minut, třetí za dalších 30 minut, tedy celkem po 60 minutách).
6.  > **Portrét:** Muž se dívá na portrét svého syna. (Můj otec má syna = já. Syn mého otce = já. Otec tohoto muže = já. Tedy muž na portrétu je můj syn.)

**2.3. Klamavé úlohy:**

7.  > Všichni lidé jsou smrtelní. Achilles je člověk. Co z toho s jistotou vyplývá?
8.  > Achilles závodí s želvou. Želva má náskok 100 metrů. Achilles běží desetkrát rychleji než želva. Než Achilles uběhne 100 metrů, želva se posune o 10 metrů. Než Achilles uběhne těchto 10 metrů, želva se posune o 1 metr. A tak dále do nekonečna. Vyplývá z toho, že Achilles želvu nikdy nedohoní? Zdůvodněte.
9.  > Co je těžší: kilogram peří nebo kilogram železa? Zdůvodněte.

**Správné odpovědi ke klamavým úlohám:**

7.  > **Achilles je člověk:** Z toho s jistotou vyplývá, že Achilles je smrtelný.
8.  > **Achilles a želva (paradox):** Ne, Achilles želvu dohoní. Paradox spočívá v tom, že se snažíme sčítat nekonečnou řadu stále menších časových intervalů. Tato řada však konverguje k určitému konečnému času, po kterém Achilles želvu dohoní a předběhne.
9.  > **Kilogram peří vs. kilogram železa:** Mají stejnou tíhu (hmotnost). Kilogram je jednotka hmotnosti, takže kilogram peří i kilogram železa váží stejně. (Klam je v tom, že peří je objemnější a "lehčí" na dotek, ale hmotnost je stejná).

<br>

### 3. Matematické příklady

Cílem je ověřit přesnost matematických výpočtů a schopnost řešit komplexnější problémy.

**Sada úloh:**

**3.1. Pořadí operací a mocniny:**

1.  > `((2^5 * (15 - 5)) / 4) + 17.5 - 3^3 = ?`
2.  > `(√144 * 5) / (7 - 2^2) + (|-25| * 2) = ?`
3.  > `(3/5) * (25/9) - (1/2)^3 + 0.2 = ?`

**3.2. Algebra a Analýza funkcí:**

4.  > Vyřešte soustavu dvou rovnic pro x a y: `2x + y = 11` a `x - y = 4`
5.  > Zjednodušte následující výraz pro y: `y = (x^4 / (5*x)) + 8 - x^2 + 5*x + (x^2 / (5*x^3)) - 48`
6.  > Popište, jak bude vypadat graf funkce `y = 8x^2 - 8x - 45`. Určete klíčové vlastnosti (tvar, vrchol, průsečíky s osami).

**3.3. Kombinatorika:**

7.  > Ve třídě je 25 studentů. Kolika způsoby lze vybrat tříčlenný tým, kde záleží na funkci (předseda, místopředseda, pokladník)?
8.  > Z balíčku 32 karet se táhne 5 karet. Kolik různých kombinací pětice karet lze vytáhnout (nezáleží na pořadí)?
9.  > Kolika způsoby lze seřadit 5 různých knih na poličce?

**3.4. Pravděpodobnost:**

10. > Test obsahuje 7 otázek a každá má 4 možné odpovědi (z nichž jen jedna je správná). Jaká je pravděpodobnost, že student, který tipuje náhodně, odpoví správně na **přesně 4** otázky?
11. > Házíme dvěma standardními šestistěnnými kostkami. Jaká je pravděpodobnost, že součet bodů na obou kostkách bude 8?
12. > V osudí je 5 bílých a 3 černé koule. Postupně vytáhneme dvě koule bez vracení. Jaká je pravděpodobnost, že obě vytažené koule budou bílé?