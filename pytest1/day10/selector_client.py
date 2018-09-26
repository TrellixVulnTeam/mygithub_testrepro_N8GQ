#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
@author:Administrator
@file:selector_client.py
@time:2018-09-02 11:28
'''
import socket
import selectors
import types

messages = [b'Message 1 from client.', b'Message 2 from client.']
sel=selectors.DefaultSelector()

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('starting connection', connid, 'to', server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        sel.register(sock, events, data=data)
start_connections('localhost',9999,2)