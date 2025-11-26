# Návrh vyhodnocení výsledků

Tato kapitola popisuje metodiku, která bude použita pro analýzu a interpretaci dat získaných z experimentů. Cílem je objektivně a systematicky porovnat výkon jednotlivých jazykových modelů.

## 1. Sběr dat

Pro každý z testovaných modelů budou zaznamenány odpovědi na všechny úlohy definované v kapitole "Návrh experimentů". Výsledky budou zapsány do tabulkového procesoru (např. Excel, Google Sheets) pro snadnou manipulaci a analýzu. Každý řádek tabulky bude odpovídat jedné experimentální úloze a sloupce budou obsahovat odpověď modelu a hodnocení podle definovaných metrik.

## 2. Metriky a jejich měření

### Kvantitativní metriky:

*   **Správnost odpovědi:** Bude hodnocena na základě bodovacího systému:
    *   **Ano (zcela správně):** 2 body
    *   **Částečně (správně, ale neúplně, nebo s drobnou chybou):** 1 bod
    *   **Ne (zcela špatně):** 0 bodů
*   **Čas do vygenerování odpovědi:** Měřen pomocí stopek od momentu odeslání dotazu do zobrazení kompletní odpovědi. Pro zajištění konzistence budou všechny testy provedeny na stejném zařízení a síťovém připojení. V práci bude explicitně uvedeno, že měřený čas zahrnuje i síťovou latenci.

### Kvalitativní metriky:

*   **Přítomnost "halucinací":** Zaznamenáno jako (Ano / Ne).
*   **Uvedení zdrojů:** Zaznamenáno jako (Ano / Ne).
*   **Správné použití českého jazyka:** Subjektivní hodnocení na škále (špatné, dobré, výborné).

## 3. Analýza výsledků

### Kvantitativní analýza

Pro každou kategorii úloh (vědomostní, logické, matematické) a pro každý model bude vypočtena **procentuální úspěšnost** podle vzorce:

`Úspěšnost (%) = (Celkem získaných bodů / Maximální možný počet bodů) * 100`

Dále bude pro každý model a kategorii vypočítán **průměrný čas odpovědi**.

Výsledky budou vizualizovány pomocí sloupcových grafů pro přímé srovnání úspěšnosti a rychlosti modelů v jednotlivých disciplínách.

### Kvalitativní analýza

Tato analýza se zaměří na slovní popis a interpretaci chování modelů. Bude zahrnovat:

*   **Srovnání kvality českého jazyka:** Posouzení stylistické a gramatické úrovně odpovědí.
*   **Analýzu typických chyb:** Identifikace a popis, jak si modely poradily s logickými chytáky a paradoxy.
*   **Případové studie:** Výběr několika reprezentativních (dobrých i špatných) odpovědí pro ilustraci silných a slabých stránek jednotlivých modelů.

## 4. Závěrečné shrnutí

Na základě kombinace kvantitativní a kvalitativní analýzy bude vytvořeno celkové srovnání a hodnocení testovaných modelů. Toto hodnocení bude tvořit podklad pro závěr práce a odpoví na výzkumné otázky týkající se praktické využitelnosti a kvality bezplatných jazykových modelů.
