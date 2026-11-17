#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DUVARLA DERİN SOHBET MOTORU
Versiyon: 1.0 - Duvar hala sessiz.
"""

import random
import time

def duvar_cevap_verir():
    cevaplar = [
        "...",
        "(sessizlik)",
        "Duvar derin bir nefes alır gibi yapar ama almaz.",
        "Hmmm... (aslında hmmm de demez)",
        "Seni duyuyorum... (duymuyor)",
        "Devam et, ilgileniyorum. (ilgilenmiyor)",
        "Bu çok derin bir konu. (değil)",
    ]
    return random.choice(cevaplar)

def sohbet_baslat():
    print("=" * 50)
    print("DUVARLA DERİN SOHBET MOTORU BAŞLATILDI")
    print("Duvar hazır. Sen de hazır ol. (değilsin)")
    print("=" * 50)
    print()
    
    sorular = [
        "Hayatın anlamı nedir duvar?",
        "Neden sessizsin?",
        "Bana bir şey söyle.",
        "Sen de mi yorgunsun?",
        "Bugün nasılsın?",
        "Sence ben çok mu konuşuyorum?",
        "Bir sır paylaş."
    ]
    
    for i in range(5):
        soru = random.choice(sorular)
        print(f"Sen: {soru}")
        time.sleep(1.5)
        print(f"Duvar: {duvar_cevap_verir()}")
        print()
        time.sleep(1)
    
    print("Sohbet bitti. Duvar hala orada. Sen de.")
    print("Teşekkürler duvar, harika bir terapi oldu. (olmadı)")
    
    # Gizli not: bazen duvarlar da kayyum olur, ama bu duvar değil.
    # (saklı siyasi ima: kayyumlar ve sessiz kalanlar)

if __name__ == "__main__":
    sohbet_baslat()
