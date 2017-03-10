#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect('dependencyList.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE dependencies (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO dependencies (task,status) VALUES ('Dependency: Receive Vendor1 Code',0)")
con.execute("INSERT INTO dependencies (task,status) VALUES ('Dependency: Infrastructure is built',1)")
con.execute("INSERT INTO dependencies (task,status) VALUES ('Dependency: Operational Model is supplied',1)")
con.execute("INSERT INTO dependencies (task,status) VALUES ('Dependency: More people are on-boarded',0)")
con.commit()
