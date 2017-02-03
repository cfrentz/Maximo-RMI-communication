'''
Created on 18.01.2017
test_disconnect.py
@author:  carsten.frentzqde.ibm.com
@summary: test RMI communication ( session connect / disconnect ) 
@version: 1.0

see also 
developerworks wiki - Maximo 76 : issue on RMI session.disconnect
https://www.ibm.com/developerworks/community/forums/html/topic?id=9692dbc0-e3ea-428d-a5a8-ca30f116926a

    for disconnect use below code
        SecurityServiceRemote srv=(SecurityServiceRemote) ses.lookup("SECURITY");
        srv.disconnectUser(session.getUserInfo()); 

'''

if __name__ == '__main__':

    import os
    import sys
    
    if 'java' in sys.platform.lower():
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "businessobjects.jar"))
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icu4j.jar"))
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "json4j.jar"))

    import psdi.util.MXSession as MXSession
    import psdi.util.MXException as MXException
  
    try:
        session = MXSession.getSession()
        # local vmware   : 192.168.145.131:13400/MXServer
        # remote dev env : 9.70.166.80:13400/MXS75WS (maxsup038.swg.usma.ibm.com = [9.70.166.80])
        session.setHost('192.168.145.131:13400/MXServer')
        session.setUserName('maxadmin')
        session.setPassword('maxadmin')
        session.connect()
        print 'session.connect() : successfully'
        # does not work
        # session.disconnect()
        #
        # from developerworks wiki
        # public interface ServiceRemote extends java.rmi.Remote
        # Abstracts a Service on a remote MXServer. The only reason that it is used is to provide a common superclass for casting purposes. 
        # This allows us to have generic utilities for locating and managing remote Services. 
        # The ServiceRemote is then cast to a specific remote Service, e.g. WorkFlowServiceRemote.
        remoteservice = session.lookup('SECURITY') # returns the specified remote service
        remoteservice.disconnectUser(session.getUserInfo())
        
    except MXException, conex:
        print 'session.connect() : error'
        print '  conex.getErrorGroup()     :',conex.getErrorGroup()
        print '  conex.getErrorKey()       :',conex.getErrorKey()
        print '  conex.getDetail()         :',conex.getDetail() 
        print '  conex.getDisplayMessage() :',conex.getDisplayMessage() 

        

