
﻿**AI Klinik - README**

**Ürün Fikri ve Takım İçindeki Rollerin Belgelenmesi**

**Takım İsmi**

AI Klinik Geliştiricileri

**Takım Rolleri**

- **Ürün Sahibi (Product Owner):** Proje vizyonunu belirler, backlog'u önceliklendirir ve paydaşlarla iletişimi yönetir.
- **Scrum Master:** Agile süreçlerin düzgün yürütülmesini sağlar, engelleri kaldırır.
- **Geliştirici (Developer):** Teknik gereksinimleri yerine getirir, kodlama ve test süreçlerini yürütür.
- **Tasarımcı:** Kullanıcı arayüzü (UI) ve kullanıcı deneyimi (UX) tasarımlarını hazırlar.
- **Test Uzmanı:** Yazılımın doğruluğunu ve performansını test eder.

**Ürün İsmi**

AI Klinik - Yapay Zekâ Destekli Klinik Vaka Simülasyonu

**Ürün Açıklaması**

AI Klinik, tıp fakültesi öğrencilerinin klinik düşünme becerilerini geliştirmek için yapay zekâ destekli bir web platformudur. Platform, öğrencilerin seviyesine uygun dinamik vaka senaryoları sunar, sanal hastalara sorular sorarak tanı ve tedavi süreçlerini deneyimlemelerine olanak tanır. Sistem, öğrencilerin performansını analiz ederek geri bildirim sağlar ve eğitmenlerin süreci izlemesine imkan verir.

**Ürün Özellikleri**

- **Vaka Oluşturucu AI:** Öğrencinin seviyesine göre dinamik vaka senaryoları üretir.
- **Sanal Hasta Arayüzü:** Öğrencilerin hastaya sorular sorarak bilgi toplamasını sağlar.
- **Tanı ve Tedavi Adımı:** Öğrencilerin tanı koyup tedavi önerileri sunmasına olanak tanır.
- **Otomatik Değerlendirme:** Yapay zekâ, öğrencinin performansını analiz eder ve geri bildirim sağlar.
- **Eğitmen Paneli:** Akademisyenlerin vakaları izlemesine ve puanlamasına imkan tanır.

**Hedef Kitle**

- Tıp fakültesi öğrencileri
- Tıp eğitmenleri ve akademisyenler
- Sağlık alanında simülasyon temelli eğitim veren kurumlar

**Genel Product Backlog**

Aşağıdaki tablo, projenin tüm özelliklerini kapsayan genel product backlog'u temsil eder. Toplamda 3 sprintte tamamlanması planlanmıştır. Her madde, bir geliştirici için anlaşılır ve uygulanabilir olacak şekilde sadeleştirilmiştir.

|**ID**|**User Story**|**Açıklama**|**Puan**|**Öncelik**|
| :-: | :-: | :-: | :-: | :-: |
|US01|Kullanıcı olarak, platforma giriş yapabilmek istiyorum ki vaka simülasyonlarına erişebileyim.|Temel bir giriş ekranı (kullanıcı adı ve şifre ile) ve oturum açma fonksiyonu geliştirilecek.|20|Yüksek|
|US02|Kullanıcı olarak, ana sayfada mevcut vaka senaryolarını liste halinde görebilmek istiyorum.|Ana sayfada statik bir vaka listesi (örneğin, 3-4 vaka başlığı) gösterilecek.|15|Yüksek|
|US03|Kullanıcı olarak, bir vaka seçtiğimde vaka detaylarını görebilmek istiyorum.|Seçilen vakanın temel bilgileri (hasta adı, yaş, şikayet) statik bir sayfada gösterilecek.|15|Orta|
|US04|Geliştirici olarak, projenin temel backend yapısını kurmak istiyorum ki ileride dinamik özellikler eklenebilsin.|Basit bir Python/Flask server kurulumu ve temel bir veritabanı bağlantısı (örneğin, SQLite).|20|Yüksek|
|US05|Kullanıcı olarak, sanal hastaya basit sorular sorabilmek istiyorum ki vaka hakkında bilgi toplayabileyim.|Sabit bir soru listesi (örneğin, 5 soru) ve statik cevaplar içeren bir arayüz geliştirilecek.|20|Orta|
|US06|Kullanıcı olarak, platformun temel arayüzünün temiz ve anlaşılır olmasını istiyorum.|Basit bir HTML/CSS arayüzü (Bootstrap veya Tailwind kullanılarak) tasarlanacak.|10|Orta|
|US07|Kullanıcı olarak, bir vakayı çözmek için tanı ve tedavi önerisi girebilmek istiyorum.|Tanı ve tedavi için bir metin giriş alanı ve kaydetme butonu içeren bir arayüz geliştirilecek.|20|Orta|
|US08|Kullanıcı olarak, vaka çözümümün yapay zekâ tarafından değerlendirildiğini görmek istiyorum.|Basit bir puanlama sistemi (örneğin, doğru/yanlış cevaplara göre sabit geri bildirim) geliştirilecek.|25|Orta|
|US09|Eğitmen olarak, öğrencilerin vaka çözümlerini liste olarak görebilmek istiyorum.|Eğitmen panelinde öğrenci çözümlerini listeleyen statik bir sayfa geliştirilecek.|15|Orta|
|US10|Eğitmen olarak, bir öğrencinin vaka çözümüne puan verebilmek istiyorum.|Eğitmen panelinde puanlama için bir metin giriş alanı ve kaydetme butonu eklenecek.|15|Orta|
|US11|Geliştirici olarak, vaka oluşturucu AI için temel bir algoritma geliştirmek istiyorum ki dinamik vakalar üretilebilsin.|Basit bir algoritma ile rastgele vaka verileri (hasta bilgileri, şikayetler) üretilecek.|30|Yüksek|
|US12|Kullanıcı olarak, vaka sorularına dinamik cevaplar almak istiyorum ki daha gerçekçi bir deneyim yaşayayım.|Sorulara AI tabanlı dinamik cevaplar üreten bir sistem geliştirilecek (basit bir kural tabanlı sistem).|25|Yüksek|
|US13|Kullanıcı olarak, platformun mobil uyumlu olmasını istiyorum ki farklı cihazlarda kullanabileyim.|Arayüzün responsive (mobil uyumlu) hale getirilmesi için CSS düzenlemeleri yapılacak.|15|Orta|
|US14|Geliştirici olarak, veritabanında kullanıcı ve vaka verilerini saklamak istiyorum ki bilgiler kalıcı olsun.|Kullanıcı ve vaka verilerini saklamak için Python/Flask ile veritabanı şeması tasarlanacak ve uygulanacak.|20|Yüksek|
|US15|Kullanıcı olarak, geçmiş vaka çözümlerimi görebilmek istiyorum ki ilerlememi takip edeyim.|Kullanıcı için geçmiş çözümlerin listelendiği bir sayfa geliştirilecek.|15|Orta|

**Toplam Puan:** 240

**Sprint 1 Product Backlog**

Sprint 1, toplam 100 puan olacak şekilde planlanmıştır. Aşağıdaki user story'ler, projenin temel altyapısını ve kullanıcı arayüzünün başlangıcını oluşturmak için seçilmiştir.

|**ID**|**User Story**|**Açıklama**|**Puan**|**Öncelik**|
| :-: | :-: | :-: | :-: | :-: |
|US01|Kullanıcı olarak, platforma giriş yapabilmek istiyorum ki vaka simülasyonlarına erişebileyim.|Temel bir giriş ekranı (kullanıcı adı ve şifre ile) ve oturum açma fonksiyonu geliştirilecek.|20|Yüksek|
|US02|Kullanıcı olarak, ana sayfada mevcut vaka senaryolarını liste halinde görebilmek istiyorum.|Ana sayfada statik bir vaka listesi (örneğin, 3-4 vaka başlığı) gösterilecek.|15|Yüksek|
|US03|Kullanıcı olarak, bir vaka seçtiğimde vaka detaylarını görebilmek istiyorum.|Seçilen vakanın temel bilgileri (hasta adı, yaş, şikayet) statik bir sayfada gösterilecek.|15|Orta|
|US04|Geliştirici olarak, projenin temel backend yapısını kurmak istiyorum ki ileride dinamik özellikler eklenebilsin.|Basit bir Python/Flask server kurulumu ve temel bir veritabanı bağlantısı (örneğin, SQLite).|20|Yüksek|
|US06|Kullanıcı olarak, platformun temel arayüzünün temiz ve anlaşılır olmasını istiyorum.|Basit bir HTML/CSS arayüzü (Bootstrap veya Tailwind kullanılarak) tasarlanacak.|10|Orta|
|US14|Geliştirici olarak, veritabanında kullanıcı ve vaka verilerini saklamak istiyorum ki bilgiler kalıcı olsun.|Kullanıcı ve vaka verilerini saklamak için Python/Flask ile veritabanı şeması tasarlanacak ve uygulanacak.|20|Yüksek|

**Toplam Puan:** 100

**Sprint 1 Notları**

**Tahmin Edilen Puan ve Tamamlanan Puan**

- **Tahmin Edilen Puan:** 100
- **Tamamlanan Puan:** 100

**Puan Tamamlama Mantığı**

- Her user story için belirlenen puanlar, işin karmaşıklığına, geliştirme süresine ve bağımlılıklarına göre tahmin edilmiştir.
- Puanlama, Fibonacci dizisi benzeri bir yaklaşımla yapılmıştır (5, 10, 15, 20 gibi).
- Bir user story tamamlandığında, ilgili puan tamamlanmış kabul edilir.

**Daily Scrum**

- Daily Scrum toplantıları her gün 15 dakika süreyle yapılacak.
- Toplantı notları bir metin dosyasında saklanacak ve gerektiğinde paylaşılacak.
- Örnek: *DailyScrum 30 Haziran - 6 Temmuz.txt* dosyasında saklanacak.

**Sprint Board Güncellemeleri**

- Sprint board, Trello kullanılarak yönetilecek. Her user story için bir kart oluşturulacak ve "Yapılacak", "Devam Ediyor", "Tamamlandı" sütunlarına taşınacak.
- Sprint sonunda board'un ekran görüntüsü alınarak README’ye eklenecek.

![image](https://github.com/user-attachments/assets/f72b1aef-5e9c-4f5b-bfd1-9ad3a33ce7f6)

**Ürün Ekran Görüntüsü**

- Sprint sonunda, geliştirilen giriş ekranı, ana sayfa ve vaka detay sayfalarının ekran görüntüleri eklenecek.

![image](https://github.com/user-attachments/assets/181c8d15-ec01-4b4f-aaf8-226c348dc2ab)
![image](https://github.com/user-attachments/assets/d55fd081-3c0a-47e4-a0bf-2a868d1b73b8)
![image](https://github.com/user-attachments/assets/98540fa7-c589-4927-aff1-dcb9faf7f435)

**Sprint 1 Özeti**

- Sprint 1, 100 puanlık hedefiyle başarıyla tamamlandı. Tamer, Adnan ve Şahide, Betül’ün Scrum Master liderliğinde US01, US02, US03, US04, US06 ve US14’ü teslim etti. Daily Scrum’larla ilerleme takip edildi, Trello board’u güncel tutuldu. SQLite ve API bağımlılıklarındaki küçük engeller hızlıca çözüldü. Arayüz mobil uyumlu, backend stabil hale geldi. Ekip, Sprint Review ve Retrospektif’e hazır, proje sağlam bir temel kazandı.

**Sprint Review**

- Sprint sonunda, tamamlanan user story’ler paydaşlarla gözden geçirilecek.
- Geliştirilen özellikler (giriş ekranı, vaka listesi, vaka detayları, vb.) sunulacak ve geri bildirim alınacak.

**Sprint Retrospektif**

- Sprint sonunda takım, süreçteki başarıları ve geliştirilmesi gereken noktaları tartışacak.

**Sprint 2 Product Backlog**

Sprint 2, toplam 110 puan olacak şekilde planlanmıştır. Aşağıdaki user story'ler, vaka simülasyonunun temel işlevselliğini geliştirmek için seçilmiştir.

|**ID**|**User Story**|**Açıklama**|**Puan**|**Öncelik**|
| :-: | :-: | :-: | :-: | :-: |
|US05|Kullanıcı olarak, sanal hastaya basit sorular sorabilmek istiyorum ki vaka hakkında bilgi toplayabileyim.|Sabit bir soru listesi (örneğin, 5 soru) ve statik cevaplar içeren bir arayüz geliştirilecek.|20|Orta|
|US07|Kullanıcı olarak, bir vakayı çözmek için tanı ve tedavi önerisi girebilmek istiyorum.|Tanı ve tedavi için bir metin giriş alanı ve kaydetme butonu içeren bir arayüz geliştirilecek.|20|Orta|
|US08|Kullanıcı olarak, vaka çözümümün yapay zekâ tarafından değerlendirildiğini görmek istiyorum.|Basit bir puanlama sistemi (örneğin, doğru/yanlış cevaplara göre sabit geri bildirim) geliştirilecek.|25|Orta|
|US11|Geliştirici olarak, vaka oluşturucu AI için temel bir algoritma geliştirmek istiyorum ki dinamik vakalar üretilebilsin.|Basit bir algoritma ile rastgele vaka verileri (hasta bilgileri, şikayetler) üretilecek.|30|Yüksek|
|US13|Kullanıcı olarak, platformun mobil uyumlu olmasını istiyorum ki farklı cihazlarda kullanabileyim.|Arayüzün responsive (mobil uyumlu) hale getirilmesi için CSS düzenlemeleri yapılacak.|15|Orta|

**Toplam Puan:** 110

**Sprint 2 Notları**

**Tahmin Edilen Puan ve Tamamlanan Puan**

- **Tahmin Edilen Puan:** 110
- **Tamamlanan Puan:** 110

**Puan Tamamlama Mantığı**

- Her user story için belirlenen puanlar, işin karmaşıklığına, geliştirme süresine ve bağımlılıklarına göre tahmin edilmiştir.
- Puanlama, Fibonacci dizisi benzeri bir yaklaşımla yapılmıştır (15, 20, 25, 30 gibi).
- Bir user story tamamlandığında, ilgili puan tamamlanmış kabul edilir.

**Daily Scrum**

- Daily Scrum toplantıları her gün 15 dakika süreyle yapılacak.
- Toplantı notları bir metin dosyasında saklanacak ve gerektiğinde paylaşılacak.
- Örnek: *DailyScrum 7 Temmuz - 13 Temmuz.txt* dosyasında saklanacak.

**Sprint Board Güncellemeleri**

- Sprint board, Trello kullanılarak yönetilecek. Her user story için bir kart oluşturulacak ve "Yapılacak", "Devam Ediyor", "Tamamlandı" sütunlarına taşınacak.
- Sprint sonunda board'un ekran görüntüsü alınarak README’ye eklenecek.

<img width="1845" height="860" alt="image" src="https://github.com/user-attachments/assets/1b63ef4e-bc79-4349-802b-8122b7931a26" />

**Ürün Ekran Görüntüsü**

- Sprint sonunda, geliştirilen özelliklerin ekran görüntüleri eklenecek.

<img width="1832" height="864" alt="image" src="https://github.com/user-attachments/assets/92da288a-2877-4677-8313-8566e35640cd" />
<img width="1851" height="855" alt="image" src="https://github.com/user-attachments/assets/c67a0671-6dfc-4f14-80b3-f611d6f48db8" />
<img width="1054" height="853" alt="image" src="https://github.com/user-attachments/assets/56d63bae-42dc-4b0c-a6e4-26e365a82b66" />

**Sprint 2 Özeti**

- Sprint 2, 110 puanlık hedefiyle başarıyla tamamlandı. Ekip, AI entegrasyonu ve mobil uyumluluk üzerinde odaklandı. US05, US07, US08, US11 ve US13 başarıyla teslim edildi. Daily Scrum’larla ilerleme takip edildi, Trello board’u güncel tutuldu. API entegrasyonundaki küçük sorunlar hızlıca çözüldü. Arayüz daha responsive hale geldi. Ekip, Sprint Review ve Retrospektif’e hazır, proje şimdi dinamik vaka oluşturma ve değerlendirme özelliklerine sahip.

**Sprint Review**

- Sprint sonunda, tamamlanan user story’ler paydaşlarla gözden geçirilecek.
- Geliştirilen özellikler (soru sorma, tanı koyma, AI değerlendirme, vaka oluşturma, mobil uyum) sunulacak ve geri bildirim alınacak.

**Sprint Retrospektif**

- Sprint sonunda takım, süreçteki başarıları ve geliştirilmesi gereken noktaları tartışacak.

- Başarılar: AI entegrasyonu sorunsuz çalıştı, mobil uyum hızlı tamamlandı.
- Geliştirme Alanları: JSON parsing daha güvenli hale getirilebilir, test coverage artırılabilir.
