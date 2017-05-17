from django.shortcuts import render
from conectar.models import mcafee_updatedstate
from django.template import Context, loader
import MySQLdb
from django.http import HttpResponse
from django.db import connection
from os import getenv
import pymssql
from django.shortcuts import render
from math import sin #para usar la funci?n seno
import numpy as np
from time import time
from .forms import entrausuario,umbrales
from django.http import HttpResponseRedirect
def insertarusuario(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = entrausuario(request.POST)
        # check whether it's valid:
        print request.POST.get('firstname')

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = entrausuario()

    return render(request, 'postgres/form.html', {'form': form})

def index5(request):
    i = 0
    conn = pymssql.connect("57.228.130.162\AV_BR", "Accenture", "Accenture.brdb4", "ePO4_8KPRVEPO02")
    cursor = conn.cursor()
    cursor.execute("SELECT UPPER(RIGHT(' ' + EPOComputerProperties.UserProperty1, -1 + CHARINDEX(' ',REVERSE(' ' + EPOComputerProperties.UserProperty1)))) as serial,UPPER(EPOComputerProperties.ComputerName) as hostname,EPOComputerProperties.IPAddress as ip,LEFT(EPOComputerProperties.IPAddress, LEN(EPOComputerProperties.IPAddress) - CHARINDEX('.',REVERSE (EPOComputerProperties.IPAddress))) as node,EPOComputerProperties.OSType as os_name,EPOProductProperties.DATVer as dat_ver,CAST(EPOProductProperties.DATDate as DATETIME) as mcafee_last_connection,0 as mcafee FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.DATVer NOT IN (SELECT DISTINCT top 5 EPOProductProperties.DATVer FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID ORDER BY EPOProductProperties.DATVer DESC) and EPOProductProperties.ProductCode like '%VIRUSCAN%' AND EPOComputerProperties.ParentID = EPOProductProperties.ParentID AND EPOComputerProperties.ComputerName IS NOT NULL  AND EPOComputerProperties.ComputerName <> '' union SELECT UPPER(RIGHT(' ' + EPOComputerProperties.UserProperty1, -1 + CHARINDEX(' ',REVERSE(' ' + EPOComputerProperties.UserProperty1)))) as serial, UPPER(EPOComputerProperties.ComputerName) as hostname,EPOComputerProperties.IPAddress as ip,LEFT(EPOComputerProperties.IPAddress, LEN(EPOComputerProperties.IPAddress) - CHARINDEX('.',REVERSE (EPOComputerProperties.IPAddress))) as node,EPOComputerProperties.OSType as os_name,EPOProductProperties.DATVer as dat_ver,CAST(EPOProductProperties.DATDate as DATETIME) as mcafee_last_connection,1 as mcafee FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.DATVer IN (SELECT DISTINCT top 5 EPOProductProperties.DATVer FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID ORDER BY EPOProductProperties.DATVer DESC) and EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID AND EPOComputerProperties.ComputerName IS NOT NULL  AND EPOComputerProperties.ComputerName <> ''")
    for row in cursor:
        print i
        print('row = %r' % (row,))
        i = i + 1
    conn.close()
    return HttpResponse(row)

def index3(request):
    inventario = []
    tiempo_inicial = time() 
    tiempo_final = time() 
    i = 0
    xa = 0;
    xd = 0;
    conn = pymssql.connect("57.228.130.162\AV_CL", "Accenture", "Accenture.dbcl", "ePO4_8KPRVEPO01")
    cursor = conn.cursor()
    cursor.execute("SELECT UPPER(RIGHT(' ' + EPOComputerProperties.UserProperty1, -1 + CHARINDEX(' ',REVERSE(' ' + EPOComputerProperties.UserProperty1)))) as serial,UPPER(EPOComputerProperties.ComputerName) as hostname,EPOComputerProperties.IPAddress as ip,LEFT(EPOComputerProperties.IPAddress, LEN(EPOComputerProperties.IPAddress) - CHARINDEX('.',REVERSE (EPOComputerProperties.IPAddress))) as node,EPOComputerProperties.OSType as os_name,EPOProductProperties.DATVer as dat_ver,CAST(EPOProductProperties.DATDate as DATETIME) as mcafee_last_connection,0 as mcafee FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.DATVer NOT IN (SELECT DISTINCT top 5 EPOProductProperties.DATVer FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID ORDER BY EPOProductProperties.DATVer DESC) and EPOProductProperties.ProductCode like '%VIRUSCAN%' AND EPOComputerProperties.ParentID = EPOProductProperties.ParentID AND EPOComputerProperties.ComputerName IS NOT NULL  AND EPOComputerProperties.ComputerName <> '' union SELECT UPPER(RIGHT(' ' + EPOComputerProperties.UserProperty1, -1 + CHARINDEX(' ',REVERSE(' ' + EPOComputerProperties.UserProperty1)))) as serial, UPPER(EPOComputerProperties.ComputerName) as hostname,EPOComputerProperties.IPAddress as ip,LEFT(EPOComputerProperties.IPAddress, LEN(EPOComputerProperties.IPAddress) - CHARINDEX('.',REVERSE (EPOComputerProperties.IPAddress))) as node,EPOComputerProperties.OSType as os_name,EPOProductProperties.DATVer as dat_ver,CAST(EPOProductProperties.DATDate as DATETIME) as mcafee_last_connection,1 as mcafee FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.DATVer IN (SELECT DISTINCT top 5 EPOProductProperties.DATVer FROM EPOProductProperties,EPOComputerProperties where EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID ORDER BY EPOProductProperties.DATVer DESC) and EPOProductProperties.ProductCode like '%VIRUSCAN%' and EPOComputerProperties.ParentID = EPOProductProperties.ParentID AND EPOComputerProperties.ComputerName IS NOT NULL  AND EPOComputerProperties.ComputerName <> ''")
    for row in cursor:
        inventario.append(row[1])
        if row[7] == 0:
            xd = xd + 1
        if row[7] == 1:
            xa = xa + 1    
        i = i + 1
        print('row = %r' % (row,))
    print inventario     
    print 'total'   
    print i
    print 'act'
    print xa
    print 100 * xa / i
    print 'desac'
    print xd
    print 100 - (100 * xa / i)
    conn.close()
    db = MySQLdb.connect("10.10.12.21","remoteocs","remoteocs","ocsweb" )
    cursor = db.cursor()
    cursor.execute("select hardware.NAME,bios.SSN,bios.BMANUFACTURER,bios.SMODEL,hardware.modelo,hardware.USERID,hardware.LASTDATE,accountinfo.TAG,hardware.OSNAME,hardware.WORKGROUP from hardware,bios,accountinfo where hardware.ID = accountinfo.HARDWARE_ID and hardware.ID = bios.HARDWARE_ID")
    t = 0
    b = 0
    c = 0
    for row in cursor:
        t = t + 1
        print row[0]
        if str(row[0]) not in inventario:
            b = b + 1
        if str(row[0]) in inventario:
            c = c + 1
        
    print 'totol osc = ' + str(t)
    print 'total  no mcafee = ' + str(b)
    print 'total mcafee = ' + str(c)
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    db = MySQLdb.connect("localhost","root","123456","iess_schema" )
    cursor = db.cursor()
    cursor.execute("INSERT INTO `mcafee_updatedstate`(`fechaingreso`,`total`,`updated`,`noupdated`,`totalproceso`,`db`,`DATAORIGEN_id`)VALUES(NOW(),"+str(i)+","+str(xa)+","+str(xd)+","+str(tiempo_ejecucion)+",1,2)")
    db.commit()
    db.close()
    return HttpResponse(row)

def set(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = umbrales(request.POST)
        # check whether it's valid:
        print request.POST.get('uno')

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = umbrales()

    return render(request, 'postgres/set.html', {'form': form})

def index(request):
    tabla = mcafee_updatedstate.objects.latest('fechaingreso')
    return render(request, 'postgres/index.html', {'param': tabla })

def umanager(request):
    return render(request, 'postgres/form.html')