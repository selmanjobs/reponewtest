#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

secenek1 = "(1) toplama"
secenek2 = "(2) çıkarma"
secenek3 = "(3) çarpma"
secenek4 = "(4) bölme"

print secenek1
print secenek2
print secenek3
print secenek4

soru = raw_input("Yapılacak işlemin numarasını girin: ")

if soru == "1":
     sayi1 = input("Toplama için ilk sayıyı girin: ")
     print sayi1
     sayi2 = input("Toplama için ikinci sayıyı girin: ")
     print sayi1, "+", sayi2, ":", sayi1 + sayi2
if soru == "2":
     sayi3 = input("Çıkarma için ilk sayıyı girin: ")
     print sayi3
     sayi4 = input("Çıkarma için ikinci sayıyı girin: ")
     print sayi3, "-", sayi4, ":", sayi3 - sayi4
if soru == "3":
     sayi5 = input("Çarpma için ilk sayıyı girin: ")
     print sayi5
     sayi6 = input("Çarpma için ikinci sayıyı girin: ")
     print sayi5, "x", sayi6, ":", sayi5 * sayi6
if soru == "4":
     sayi7 = input("Bölme için ilk sayıyı girin: ")
     print sayi7
     sayi8 = input("Bölme için ikinci sayıyı girin: ")
     print sayi7, "/", sayi8, ":", sayi7 / sayi8
