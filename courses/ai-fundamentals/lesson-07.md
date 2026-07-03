---
title: Paieška, įterpiniai, RAG ir agentai
module: Pažangios idėjos
order: 7
---

# Paieška, įterpiniai, RAG ir agentai

Nebūtina būti programuotoju, kad suprastum svarbiausias pažangias DI idėjas. Jos paaiškina, kodėl vieni įrankiai atsako tiksliau, kaip DI dirba su dokumentais ir kodėl kai kurios sistemos gali atlikti veiksmus.

**Po šios pamokos galėsi:**

- paprastais žodžiais paaiškinti įterpinius, RAG ir agentus;
- suprasti, kodėl RAG atsakymo kokybė priklauso nuo paieškos, o ne tik nuo modelio;
- įvardyti, kokių ribų reikia agentams.

## Įterpiniai: prasmė kaip skaičiai

**Įterpinys** tekstą paverčia skaičių sąrašu, kuris apytiksliai užfiksuoja prasmę. Panašios mintys atsiduria arti viena kitos.

```text
„kaip atšaukti prenumeratą“
ir
„noriu nutraukti mokamą planą“

gali būti arti pagal prasmę, nors žodžiai skirtingi.
```

Dėl to DI sistemos gali ieškoti pagal prasmę, o ne tik pagal tikslius raktažodžius.

## RAG: atsakymai iš tavo dokumentų

**RAG** reiškia paieška papildytą generaciją. Sistema:

1. suskaido dokumentus į dalis;
2. paverčia dalis įterpiniais;
3. pagal tavo klausimą randa aktualiausias dalis;
4. įdeda jas į modelio kontekstą;
5. paprašo atsakyti remiantis rastu tekstu.

Tai naudinga, kai nori, kad DI atsakytų iš konkrečių dokumentų: kurso medžiagos, įmonės taisyklių, produkto instrukcijų ar tyrimų.

## Kodėl RAG nėra magija

RAG kokybė priklauso nuo:

- dokumentų kokybės;
- kaip jie suskaidyti;
- ar paieška rado tinkamas dalis;
- ar modelis laikosi instrukcijos remtis šaltiniais;
- ar atsakymas pateikia nuorodas ar citatas.

Jei paieška randa netinkamą tekstą, modelis gali atsakyti blogai net būdamas labai galingas.

## Agentai: DI, kuris gali veikti

**Agentas** yra DI sistema, kuri ne tik atsako tekstu, bet ir naudoja įrankius: paiešką, skaičiuotuvą, kalendorių, el. paštą, kodą, duomenų bazę.

Paprastas agento ciklas:

```text
Tikslas -> planas -> įrankio naudojimas -> rezultato patikrinimas -> kitas žingsnis
```

Agentai tinka kelių žingsnių užduotims, bet jiems reikia ribų:

- veiksmų limito;
- leidžiamų įrankių sąrašo;
- žmogaus patvirtinimo prieš rizikingus veiksmus;
- žurnalų, kad matytum, ką agentas darė.

## Pasitikrink save

**1. Kam reikalingi įterpiniai?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Jie paverčia tekstą skaičiais, kurie užfiksuoja prasmę, todėl sistema gali ieškoti pagal prasmę („atšaukti prenumeratą“ ≈ „nutraukti mokamą planą“), o ne tik pagal tikslius žodžius.

</details>

**2. Kodėl galingas modelis su RAG vis tiek gali atsakyti blogai?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Jei paieška surado ne tas dokumentų dalis, modelis atsako remdamasis netinkamu tekstu. RAG kokybė priklauso nuo dokumentų, jų suskaidymo ir paieškos — ne vien nuo modelio.

</details>

**3. Kuo agentas skiriasi nuo paprasto pokalbių asistento ir kokių ribų jam reikia?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Agentas ne tik atsako tekstu, bet ir atlieka veiksmus įrankiais. Todėl jam reikia veiksmų limito, leidžiamų įrankių sąrašo, žmogaus patvirtinimo prieš rizikingus veiksmus ir žurnalų.

</details>

## Mini užduotis

Įsivaizduok DI asistentą, kuris padėtų tau vienoje srityje: mokytis, planuoti keliones, tvarkyti biudžetą, rašyti, sportuoti. Užrašyk:

- kokius dokumentus jis turėtų naudoti;
- kokius įrankius galėtų turėti;
- kokiems veiksmams reikėtų tavo patvirtinimo.

> **Užduoties patikra:** aprašyk savo įsivaizduojamą asistentą mentoriui ir paklausk: „Įvertink mano asistento planą: ar ribos pakankamos, kokių rizikų nepastebėjau?“

> **Mentoriaus patarimas:** paklausk „Paaiškink RAG ir agentus be techninių terminų, su kasdieniu pavyzdžiu.“

Toliau: sujungsime viską į kasdienį DI darbo procesą.
