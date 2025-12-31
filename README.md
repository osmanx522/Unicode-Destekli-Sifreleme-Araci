# ASCII & Unicode Cipher Tool 🔐

Bu proje, metin tabanlı verileri ASCII ve Unicode standartlarını kullanarak sayısal formatlara dönüştüren (şifreleyen) ve dosyadan okuyarak tekrar eski haline getiren (deşifre eden) bir Python uygulamasıdır. 

Özellikle **veri bütünlüğü** ve **Unicode karakter desteği** (Emoji, Türkçe karakterler vb.) üzerine odaklanılarak geliştirilmiştir.

## 🚀 Proje Hakkında

Bu araç, girilen herhangi bir metni (String) bilgisayarın anlayabileceği sayısal değerlere (Decimal) dönüştürür. Savunma sanayi ve veri işleme alanındaki **veri serileştirme** (serialization) ve **sabit genişlikli kodlama** (fixed-width encoding) mantığını kavramak amacıyla geliştirilmiştir.

## ✨ Özellikler

* **Tam Unicode Desteği:** Türkçe karakterler (ç, ş, ğ) ve Emojis (🚀, 😊) sorunsuz işlenir.
* **Sabit Genişlikli Kodlama:** Her karakter, veri bütünlüğünü korumak için 7 haneli standart bir formata dönüştürülür.
* **Dosya İşlemleri (I/O):** Şifrelenen veriler `.txt` dosyasına kaydedilir ve oradan okunur.
* **Modüler Yapı:** Şifreleme, dosya okuma/yazma ve deşifreleme işlemleri ayrı fonksiyonlarda ele alınmıştır.

## ⚙️ Algoritma Mantığı

Sistem şu adımları izler:

1.  **Girdi:** Kullanıcıdan bir metin alınır. (Örn: `A`)
2.  **Dönüşüm:** Karakterin Unicode sayısal karşılığı bulunur. (`ord('A')` -> `65`)
3.  **Formatlama (Padding):** Sayı, 7 basamağa tamamlanana kadar soluna sıfır eklenir. (`0000065`)
    * *Neden 7 basamak?* Standart ASCII karakterleri dışında, yüksek bitli Unicode karakterlerini ve emojileri de kapsamak için maksimum sınır baz alınmıştır.
4.  **Kaydetme:** Oluşan sayısal dizi dosyaya yazılır.

## 🛠️ Kurulum ve Kullanım

Projeyi bilgisayarınızda çalıştırmak için Python 3.x yüklü olmalıdır.

1.  Repoyu klonlayın (veya indirin):
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/repo-ismin.git](https://github.com/KULLANICI_ADIN/repo-ismin.git)
    ```
2.  Proje dizinine gidin ve çalıştırın:
    ```bash
    python encryption.py --> Metni Şifreler
    veya
    python decryption.py --> Şifreyi Çözer
    ```
3.  Ekrandaki yönergeleri izleyin.
## 🔮 Gelecek Güncellemeler (Roadmap)
[ ] Veri boyutunu düşürmek için "Sabit Genişlik" yerine "Ayıraçlı (Delimiter)" yapıya geçilmesi (CSV mantığı).

[ ] Kullanıcı arayüzü (GUI) eklenmesi.

[ ] Şifreleme algoritmasının matematiksel işlemlerle (Sezar, XOR) güçlendirilmesi.
