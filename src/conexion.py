#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-

__author__ = "jcarlos"
__date__ = "$27-oct-2015 11:30:50$"

import sqlite3

try:
    bd = sqlite3.connect("tallerauto.sqlite")
    print ("Conexion correcta con la base de datos.")
except:
    print("No se pudo establecer conexion con el servidor.")
    exit