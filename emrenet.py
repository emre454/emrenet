import scapy.all as scapy
from scapy.all import ARP, Ether, srp
import os
import subprocess
import sys
import optparse
import re

def ip_format_kontrol(ip):
    regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.' \
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' \
            r'(/([8-9]|[12][0-9]|3[0-2]))?$'
    
    if re.match(regex, ip):
        return True
    else:
        return False
def root():

    if os.getuid() != 0:

        print("(｀・ω・´) Lütfen root olarak çalıştırın")
        subprocess.call(["sudo", "python3"] + sys.argv)  
        sys.exit()  


def tara():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ipadres",dest="ip",help="Lütfen taramak istediğiniz ağın IP adresini girin. Örnek: 192.168.1.1/24 veya 10.0.0.0/16 şeklinde.\n IP adresinin sonunda '/CIDR' formatında bir ağ maskesi belirtilebilir. Örneğin, /24, /16 gibi. Bu seçenekle bir IP adresi veya ağ aralığı belirtmelisiniz.\n Ayrıca, IP adresinin doğru formatta olup olmadığını kontrol ettiğinizden emin olun: Örnek: 192.168.1.1/24")
    (cevaplar,cevapsizlar)= parser.parse_args()
    ip=cevaplar.ip
    
    if ip is None:
        print("(・ω・) Hmm... IP adresini unuttun galiba! Lütfen -i parametresi ile bir IP adresi yaz! Örnek: 192.168.1.1/24 ")
        print("Yardım almak için: python emrenet.py -h veya --help kullanabilirsiniz.")
        return []
    if not ip_format_kontrol(ip):
        print("(×_×;） IP adresi geçerli formatta değil! Lütfen doğru formatta gir! Örnek: 192.168.1.1/24")
        print("Yardım almak için: python emrenet.py -h veya --help kullanabilirsiniz.")
    arp_cevap= scapy.ARP(pdst=ip)

    yayin= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_cevap_yayini= yayin/arp_cevap
    cevaplar_listesi =scapy.srp(arp_cevap_yayini,timeout=1, verbose = False)[0]


    liste=[]
    for elaman in cevaplar_listesi:
        liste_sozluk={"ip":elaman[1].psrc,"mac":elaman[1].hwsrc}
        liste.append(liste_sozluk)
    return liste
def fonksiyon_print(print_fonksiyon):
    print("IP\t\t\tMac Adres \n *******************************************************")
    for istemci in print_fonksiyon:
        print(istemci["ip"]+"\t\t"+istemci["mac"])






root()
tara_sonuc= tara()
if tara_sonuc:
    fonksiyon_print(tara_sonuc)

