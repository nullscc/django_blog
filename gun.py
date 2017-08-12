# -*- coding: utf-8 -*-
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = False 
loglevel = 'info'
bind = '127.0.0.1:5000'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
