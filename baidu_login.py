#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Wujie.Cheng'

import random
def gid_encrypt():
    s_raw = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    s_ret = ''
    for s in s_raw:
        t = random.randint(0, 16)
        if 'x' == s:
            n = t
            s_ret += hex(n)[-1:]
        elif 'y' == s:
            n =  3 & t | 8
            s_ret += hex(n)[-1:]
        else:
            s_ret += s
    return s_ret.upper()
print(gid_encrypt())
import rsa
import binascii
def rsa_encrypt(message, rsa_n, rsa_e='10001'):
    rsa_e = int(rsa_e, 16)
    rsa_n = int(rsa_n, 16)
    key = rsa.PublicKey(rsa_n, rsa_e)  # 创建公钥
    message = rsa.encrypt(message, key)  # 加密
    message = binascii.b2a_hex(message)  # 将加密信息转换为16进制
    return message.decode()

def rsa_n_gen(pubkey):
    l = pubkey.split("\n")
    return ''.join(l[1:-2])  # 去掉列表的第一个和最后2个

import base64
pwd = '123'

pubkey = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8Xi84NDp0cJaLE59L6yINeF3Q\nr9TpcNSq2Eg\/s5O80vinCcjA+xJQL\/bEO4RT8drvrbh4hsEz1O5C3Jt0bl9GhiCP\nCo0t1fuHT66VzE0ALqYPgdBM5Od6UfMr8mD6tW28+zmhjN6++Q8DK25U16SujYaA\n0H8S0PqKlN6X\/ZHlTQIDAQAB\n-----END PUBLIC KEY-----\n'
rsa_n = rsa_n_gen(pubkey)

rsa_e = '010001'  # 和 rsa_e = '10001'  没区别

key = rsa_n_gen(pubkey)
print(key)
print(base64.b64decode(key))

def uid_encrypt():
    e = ""
    t = 0
    for n in range(32):
        if 12 == n:
            e += " "
        else:
            r = random.randint(0, 15)   # 0 <= r <= 15
            if 16 == n:
                a = 3 & r | 8
            else:
                a = r
            t += a
            e += hex(a)[2:]
    return e.replace(" ", hex(t % 16)[2:]).lower()
print(uid_encrypt())