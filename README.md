# EmreNet - Ağ Tarayıcı

**EmreNet**, Python kullanarak yerel ağda IP ve MAC adreslerini tespit etmeye yarayan bir ağ tarayıcı aracıdır. Kullanıcı, belirli bir ağ IP adresini girdiğinde, ağdaki cihazların IP ve MAC adreslerini listeleyebilir. Bu araç, ağda bağlı cihazların kimliklerini kolayca öğrenmenize yardımcı olur.

## Özellikler

- IP adresi ve ağ maskesi (CIDR) formatı ile ağ taraması yapabilirsiniz.
- IP adresinin geçerli formatta olup olmadığını kontrol eder.
- Root yetkisi gerektiren bir komut olduğundan, root olarak çalıştırmak için uygun kontrolleri yapar.
- Kullanıcı dostu hata mesajları ve ipuçları sunar.
- Ağa bağlı cihazların IP ve MAC adreslerini gösterir.

## Kurulum
Bu uygulamayı kurmak için aşağıdaki adımları takip edebilirsiniz:

1. Reposunu klonlayın:
```bash 
   git clone https://github.com/emre454/emrenet.git
```
3. Proje dizinine gidin:
4. ```bash
   cd emrenet

5. Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
6. ```
   pip install -r requirements.txt

Yardım almak için komut satırına ```bash'python emrenet.py -h'``` veya ```bash'python emrenet.py --help'``` yazabilirsiniz.
