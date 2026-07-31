---
title: Kintamieji: duomenims suteik vardus
module: 1 · Pati pradžia
order: 1
---

# Kintamieji: duomenims suteik vardus

Pirmoje pamokoje tekstą ir skaičius rašei tiesiai į `print()`. Tačiau tikros programos duomenis saugo, keičia ir naudoja keliose vietose. Tam skirti **kintamieji**.

Šioje pamokoje sukursi pirmuosius kintamuosius ir panaudosi juos mažoje programoje apie save.

## Ką išmoksi

Baigęs pamoką gebėsi:

- sukurti kintamąjį ir priskirti jam reikšmę;
- pasirinkti aiškų kintamojo pavadinimą;
- atskirti tekstą nuo skaičiaus;
- naudoti kintamuosius su `print()`;
- pakeisti išsaugotą reikšmę;
- iš kelių reikšmių sukurti aiškų sakinį.

## 1. Kas yra kintamasis?

Kintamasis yra pavadinimas, susietas su reikšme – tekstu arba skaičiumi.

```python
vardas = "Aistė"
amzius = 24
```

Ženklas `=` čia nereiškia matematinės lygybės. Python pirmiausia apskaičiuoja dešinėje esančią reikšmę, tada ją **priskiria** kairėje parašytam pavadinimui.

```text
pavadinimas = reikšmė
```

Sukūrus kintamąjį, jo pavadinimą galima naudoti vietoje pačios reikšmės:

```python
vardas = "Aistė"
print(vardas)
```

Rezultatas:

```text
Aistė
```

Atkreipk dėmesį: kuriant tekstą reikalingos kabutės, tačiau naudojant kintamąjį jų neberašome.

```python
print("vardas")  # parodo žodį: vardas
print(vardas)    # parodo kintamojo reikšmę: Aistė
```

## 2. Tekstas ir skaičiai yra skirtingos reikšmės

Python skiria tekstą nuo skaičiaus:

```python
miestas = "Kaunas"  # tekstas
metai = 2026        # sveikasis skaičius
temperatura = 21.5  # skaičius su trupmenine dalimi
```

Tai svarbu, nes su skaičiais galima skaičiuoti:

```python
amzius = 24
print(amzius + 1)
```

Rezultatas:

```text
25
```

Jei skaičių įrašytume kabutėse, jis taptų tekstu:

```python
amzius = "24"
```

Kol kas įsimink paprastą taisyklę:

- tekstas rašomas kabutėse;
- skaičius, su kuriuo skaičiuosime, rašomas be kabučių.

**Pasitikrink.** Kuri reikšmė tinka skaičiavimui – `"10"` ar `10`? Pirmiausia nuspręsk pats.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Skaičiavimui tinka `10`, nes jis parašytas be kabučių. `"10"` yra tekstas, o bandant tekstą sudėti su skaičiumi (`"10" + 1`) Python parodytų klaidą.

</details>

## 3. Kaip pavadinti kintamąjį

Geras pavadinimas trumpai paaiškina, ką saugo kintamasis:

```python
vartotojo_vardas = "Mantas"
prekes_kaina = 12.50
pamoku_skaicius = 2
```

Python kintamųjų pavadinimams taiko kelias taisykles:

- galima naudoti raides, skaitmenis ir apatinį brūkšnį `_`;
- pavadinimas negali prasidėti skaitmeniu;
- tarpų naudoti negalima;
- didžiosios ir mažosios raidės skiriasi.

```python
mano_miestas = "Vilnius"  # taisyklinga
miestas2 = "Kaunas"       # taisyklinga
2miestas = "Klaipėda"     # klaida: prasideda skaitmeniu
mano miestas = "Šiauliai" # klaida: pavadinime yra tarpas
```

Šiame kurse lietuviškus žodžius kintamųjų pavadinimuose rašysime be nosinių ir paukščiukų: `amzius`, `skaicius`, `prekes_kaina`. Taip kodą bus patogu rašyti bet kuria klaviatūra.

Venk nieko nepaaiškinančių pavadinimų:

```python
x = 12.50          # neaišku, ką reiškia x
prekes_kaina = 12.50  # paskirtis aiški
```

## 4. Viena funkcija gali gauti kelias reikšmes

Funkcijai `print()` galima perduoti kelias reikšmes, jas atskiriant kableliais:

```python
vardas = "Aistė"
miestas = "Kaunas"

print("Vardas:", vardas)
print("Miestas:", miestas)
```

Rezultatas:

```text
Vardas: Aistė
Miestas: Kaunas
```

Python tarp kableliais atskirtų dalių automatiškai įterpia tarpą. Šis būdas patogus, nes vienoje eilutėje galima rodyti ir tekstą, ir skaičių:

```python
amzius = 24
print("Man yra", amzius, "metai")
```

## 5. Kintamojo reikšmę galima pakeisti

Pavadinimas lieka tas pats, tačiau su juo susieta reikšmė gali pasikeisti:

```python
taskai = 10
print(taskai)

taskai = 15
print(taskai)
```

Rezultatas:

```text
10
15
```

Python vykdo eilutes nuo viršaus į apačią. Antrasis priskyrimas pakeičia ankstesnę `taskai` reikšmę.

Kintamąjį galima atnaujinti naudojant jo dabartinę reikšmę:

```python
taskai = 10
taskai = taskai + 5
print(taskai)
```

Dešinė pusė apskaičiuojama pirma: Python paima esamą reikšmę `10`, prideda `5` ir rezultatą `15` vėl priskiria pavadinimui `taskai`.

**Pasitikrink.** Ką išves ši programa? Nuspėk mintyse, tada patikrink.

```python
taskai = 3
taskai = taskai + taskai
print(taskai)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

`6`. Dešinė pusė apskaičiuojama pirma: `3 + 3` yra `6`, ir ši nauja reikšmė priskiriama `taskai`. Sena reikšmė `3` prarandama.

</details>

## 6. Dažnos klaidos

### Pamirštos teksto kabutės

```python
miestas = Kaunas
```

Python bando rasti kintamąjį pavadinimu `Kaunas`. Jei jis nesukurtas, gausi klaidą. Tekstui reikia kabučių:

```python
miestas = "Kaunas"
```

### Kintamasis naudojamas per anksti

```python
print(vardas)
vardas = "Aistė"
```

Python skaito nuo viršaus į apačią, todėl pirmoje eilutėje `vardas` dar neegzistuoja. Pirmiausia jį sukurk:

```python
vardas = "Aistė"
print(vardas)
```

### Nesutampa raidžių dydis

```python
vardas = "Aistė"
print(Vardas)
```

`vardas` ir `Vardas` Python kalboje yra du skirtingi pavadinimai. Patikrink, ar visur naudoji tokias pačias raides.

## 7. Praktinė užduotis

Laboratorijoje sukurk trumpą programą – savo vizitinę kortelę.

Programa turės:

1. išsaugoti vardą kintamajame `vardas`;
2. išsaugoti miestą kintamajame `miestas`;
3. išsaugoti amžių skaitiniame kintamajame `amzius`;
4. apskaičiuoti kitų metų amžių;
5. parodyti bent keturias aiškias rezultato eilutes.

Pradžia gali atrodyti taip:

```python
vardas = "Aistė"
miestas = "Kaunas"
amzius = 24
kitu_metu_amzius = amzius + 1

print("Vardas:", vardas)
print("Miestas:", miestas)
print("Dabar man:", amzius)
print("Kitais metais man bus:", kitu_metu_amzius)
```

Pakeisk pavyzdines reikšmes savomis, paleisk programą ir pateik ją automatiniams testams.

> **Užduoties patikra:** parodyk savo vizitinės kortelės kodą mentoriui ir paklausk „Ar teisingai naudoju kintamuosius savo programoje?“

## Svarbiausia iš šios pamokos

- Kintamasis yra pavadinimas, susietas su reikšme.
- Reikšmė priskiriama naudojant ženklą `=`.
- Tekstas rašomas kabutėse, o skaičius skaičiavimams – be kabučių.
- Aiškus pavadinimas padeda suprasti programą.
- Kintamojo reikšmę galima pakeisti arba apskaičiuoti iš ankstesnės reikšmės.
- Kintamąjį būtina sukurti prieš jį naudojant.

Kitoje pamokoje programa ne tik rodys paruoštus duomenis – ji išmoks paklausti vartotojo ir priimti jo atsakymą.
