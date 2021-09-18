#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

os.system("clear")
print("Select your img/iso")
a = input()
print("Select your device")
b = input()
os.system("dd if=" + a + " of=" + b)