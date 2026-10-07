# Python Portfolio

Bu repository, Python ile geliştirdiğim iki farklı projeyi içermektedir.

Bu projelerde Python'ın temel yapılarını kullanmaya, kodları anlaşılır ve düzenli tutmaya ve öğrendiğim konuları küçük uygulamalar üzerinde kullanmaya çalıştım.

Projelerden ilki terminal üzerinden çalışan bir Mini Market uygulaması, ikincisi ise PyGame Zero kullanarak geliştirdiğim basit bir 2D oyundur.

---

# 1. Mini Market

Mini Market, terminal üzerinden çalışan basit bir alışveriş uygulamasıdır.

Bu projede kullanıcı markette bulunan ürünleri görüntüleyebilir, sepetine ürün ekleyebilir veya çıkarabilir ve alışveriş sonunda ödeme işlemini gerçekleştirebilir.

## Özellikler

- Market ürünlerini ve fiyatlarını görüntüleme
- Sepete ürün ekleme
- Sepetteki ürünleri görüntüleme
- Sepetten ürün çıkarma
- Toplam alışveriş tutarını hesaplama
- Kullanıcının bütçesini kontrol etme
- Para üstünü hesaplama
- Menü üzerinden işlem seçme

## Kullanılan Python Konuları

- Değişkenler
- Listeler
- Sözlükler (Dictionary)
- `if / elif / else`
- `for` döngüsü
- `while` döngüsü
- Fonksiyonlar
- Kullanıcıdan veri alma (`input`)
- Matematiksel işlemler
- Liste metotları

## Çalıştırma

Terminal üzerinden `market_project` klasörüne girin:

```bash
cd market_project
```

Programı çalıştırın:

```bash
python3 main.py
```

---

# 2. Fruit Collector

Fruit Collector, PyGame Zero kullanarak geliştirdiğim basit bir 2D oyundur.

Bu projeyi küçük çocukların de kolayca anlayıp oynayabileceği basit ve eğlenceli bir oyun geliştirmek amacıyla hazırladım.

Oyuncunun amacı yön tuşlarını kullanarak karakteri hareket ettirmek, ekrandaki meyveleri toplamak ve düşmanlardan kaçmaktır.

## Oyun Kuralları

- Oyuncu yön tuşları ile hareket eder.
- Her toplanan meyve 1 puan kazandırır.
- Meyve toplandıktan sonra ekranda rastgele yeni bir konumda belirir.
- Ekranda hareket eden düşmanlar bulunur.
- Düşmana çarpıldığında oyuncu 1 can kaybeder.
- Oyuncu oyuna 3 can ile başlar.
- 10 meyve toplandığında oyun kazanılır.
- Can sayısı 0 olduğunda oyun sona erer.

## Kullanılan Python Konuları

- Değişkenler
- Listeler
- `for` döngüsü
- Koşullu ifadeler
- Fonksiyonlar
- Boolean değerler
- Random modülü
- Global değişkenler

## Kullanılan PyGame Zero Özellikleri

Oyundaki karakterler `Actor` kullanılarak oluşturulmuştur.

```python
player = Actor("player")
```

Karakterlerin ekrandaki konumları `pos` özelliği ile belirlenmektedir.

```python
player.pos = (350, 420)
```

Oyuncunun klavye ile hareket etmesi için PyGame Zero'nun keyboard özelliği kullanılmaktadır.

```python
if keyboard.left:
    player.x -= 5
```

Oyuncu, meyve ve düşman arasındaki çarpışmaları kontrol etmek için `colliderect()` kullanılmaktadır.

```python
if player.colliderect(fruit):
    score += 1
```

Ayrıca projede aşağıdaki PyGame Zero özellikleri kullanılmaktadır:

- `Actor`
- `pos`
- `x` ve `y`
- `draw()`
- `update()`
- `colliderect()`
- `keyboard`
- `screen.draw.text()`
- `player.left`
- `player.right`
- `player.top`
- `player.bottom`

## Kurulum

Oyunun çalışması için PyGame Zero kurulmalıdır:

```bash
pip install pgzero
```

Daha sonra `mini_game` klasörüne girin:

```bash
cd mini_game
```

Oyunu çalıştırın:

```bash
pgzrun main.py
```

## Oyun Kontrolleri

| Tuş | Hareket |
|---|---|
| ← | Sola git |
| → | Sağa git |
| ↑ | Yukarı git |
| ↓ | Aşağı git |

---

# Projelerin Amacı

Bu iki proje ile Python'ın temel programlama yapılarını farklı kullanım alanlarında uygulamayı amaçladım.

Mini Market projesinde ağırlıklı olarak kullanıcı girdileri, veri yapıları, döngüler, koşullar ve fonksiyonlar üzerinde çalıştım.

Fruit Collector projesinde ise aynı Python temellerini PyGame Zero kullanarak görsel ve interaktif bir oyun içerisinde uyguladım.

Bu sayede hem terminal tabanlı bir Python uygulaması hem de basit bir 2D oyun geliştirmiş oldum.