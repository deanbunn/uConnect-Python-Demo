#!/usr/bin/env python

from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SASL, SUBTREE, NTLM, BASE, ALL_ATTRIBUTES, Entry, Attribute, MODIFY_ADD, MODIFY_DELETE
import ldap3
import uuid
import json
import ad_common_tools

#Load AD Config
ad_config = ad_common_tools.AD_Config_Cst()

#Var for AD Filter
adFltr = "(objectclass=group)"

#AD Server
ms_ad_server = Server(ad_config.DC_Child, get_info=ALL)

#AD Connection
ms_ad_conn = Connection(ms_ad_server, user=ad_config.AD_Accnt, password=ad_config.AD_Pwd, authentication=NTLM)

#Connect to AD
if ms_ad_conn.bind():

    #Search AD 
    ms_ad_conn.search(search_base=ad_config.Path_Dept_OU, 
                      search_filter=adFltr, 
                      search_scope=SUBTREE, 
                      attributes = ["objectGuid","cn"], 
                      size_limit=0)

    #Check for Return Search Results
    if(ms_ad_conn.entries and len(ms_ad_conn.entries) > 0):
    
        print("\n")
 
        for ou_grp in ms_ad_conn.entries:    
            print(str(ou_grp.objectGuid) + "\t" + str(ou_grp.cn))

        print("\n")

    #Unbind connection to AD
    ms_ad_conn.unbind()

else:

    print('no go at this station')






