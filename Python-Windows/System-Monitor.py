#!/usr/bin/env python3

import platform
import socket
import psutil
import time
import sys
import os

class SystemMonitor:
    #
    def __init__(self):
        #
        self.service_list        = []
        self.process_list        = []
        self.memory_list         = []
        self.network_statistics  = []
        self.network_connections = []
        self.user_list           = []
        #
        '''
        <# Gather specific attributes about the system #>
        '''
        #
        self.host_name         = socket.gethostname()
        #
        self.os_type           = platform.system()
        #
        self.os_release        = platform.release()
        #
        self.os_version        = platform.version()
        #
        self.sys_architecture  = platform.uname()[4]

    def GetCPU(self):
        #
        return

    def GetMemory(self):
        #
        return

    def GetDisk(self):
        #
        return

    def GetProcess(self):
        #
        return

    def GetService(self):
        #
        services = psutil.win_service_iter()
        #
        for s in services:
            #
            service_name   = s.name()
            service_status = s.status()
            service_user   = s.username()
            service_type   = s.start_type()
            service_pid    = s.pid()
            #
            self.service_list.append([
                                         service_name,
                                         service_type,
                                         service_status,
                                         service_user,
                                         service_pid
                                     ])

    def GetNetworkStats(self):
        #
        network_stats = psutil.net_io_counters()
        #
        sent_bytes   = network_stats[0]
        recv_bytes   = network_stats[1]
        sent_packets = network_stats[2]
        recv_packets = network_stats[3]
        errors_in    = network_stats[4]
        errors_out   = network_stats[5]
        dropped_in   = network_stats[6]
        dropped_out  = network_stats[7]
        #
        self.network_statistics.append([
                                         sent_bytes,
                                         recv_bytes,
                                         sent_packets,
                                         recv_packets,
                                         errors_in,
                                         errors_out,
                                         dropped_in,
                                         dropped_out
                                      ])

    def DisplayNetworkStats(self):
        #
        while(True):
            #
            self.GetNetworkStats()
            #
            for n in self.network_statistics:
                #
                sent_bytes   = n[0]
                recv_bytes   = n[1]
                sent_packets = n[2]
                recv_packets = n[3]
                errors_in    = n[4]
                errors_out   = n[5]
                dropped_in   = n[6]
                dropped_out  = n[7]
                #
                print("[*] Ctrl+C to Exit ")
                #
                print('''
Host Network Statistics
-----------------------
Bytes Sent:                 %s
Bytes Received:             %s
Packets Sent:               %s
Packets Received:           %s
Errors (Inbound):           %s
Errors (Outbound):          %s
Packets Dropped (Inbound):  %s
Packets Dropped (Outbound): %s
                      ''' % (sent_bytes,recv_bytes,sent_packets,recv_packets,errors_in,errors_out,dropped_in,dropped_out))
                #
                time.sleep(.5)
                #
                os.system('cls')

    def GetNetworkConnections(self):
        #
        network_connections = psutil.net_connections()
        #
        ip_version               = ''
        transport_layer_protocol = ''
        local_address            = ''
        local_port               = ''
        remote_address           = ''
        remote_port              = ''
        status                   = ''
        pid                      = ''
        #
        for n in network_connections:
            #
            version   = n[1] ; version   = str(version)
            transport = n[2] ; transport = str(transport)
            #
            if('AF_INET' in version):
                #
                ip_version = 'IPV4'
                #
            if('AF_INET6' in version):
                #
                ip_version = 'IPV6'
                #
            if('SOCK_DGRAM' in transport):
                #
                transport_layer_protocol = 'UDP'
                #
            if('SOCK_STREAM' in transport):
                #
                transport_layer_protocol = 'TCP'
                #
            local_address = n[3][0]
            local_port    = n[3][1]
            #
            if(n[4]):
                #
                remote_address = n[4][0]
                #
                remote_port    = n[4][1]
                #
            else:
                #
                remote_address = 'None'
                #
                remote_port    = 'None'
                #
            status = n[5]
            #
            pid    = n[6]
            #
            self.network_connections.append([
                                                ip_version,
                                                transport_layer_protocol,
                                                local_address,
                                                local_port,
                                                remote_address,
                                                remote_port,
                                                status,
                                                pid
                                            ])

    def DisplayNetworkConnections(self):
        #
        def PrintHeaders(header_list):
            #
            for h in header_list:
                #
                print(h,end=' ')
                #
            print()
            #
            for h in headers:
                #
                for c in range(0,len(h)):
                    #
                    print('-',end='')
                    #
                print(' ',end='')
                #
            print()
            #
        while(True):
            #
            self.GetNetworkConnections()
            #
            headers = ['VER.','L4','LADDR','LPORT','RADDR','RPORT','STATUS','PID']
            #
            terminal_dimensions = os.get_terminal_size(1)
            #
            terminal_height = terminal_dimensions[1]
            #
            max_ip_version_len          = self.GetMaxLen(self.network_connections,0)
            max_transport_layer_len     = self.GetMaxLen(self.network_connections,1)
            max_local_addr_len          = self.GetMaxLen(self.network_connections,2)
            max_local_port_len          = self.GetMaxLen(self.network_connections,3)
            max_remote_addr_len         = self.GetMaxLen(self.network_connections,4)
            max_remote_port_len         = self.GetMaxLen(self.network_connections,5)
            max_status_len              = self.GetMaxLen(self.network_connections,6)
            max_pid_len                 = self.GetMaxLen(self.network_connections,7)
            #
            headers[0]   = self.PadString(headers[0],max_ip_version_len)
            headers[1]   = self.PadString(headers[1],max_transport_layer_len)
            headers[2]   = self.PadString(headers[2],max_local_addr_len)
            headers[3]   = self.PadString(headers[3],max_local_port_len)
            headers[4]   = self.PadString(headers[4],max_remote_addr_len)
            headers[5]   = self.PadString(headers[5],max_remote_port_len)
            headers[6]   = self.PadString(headers[6],max_status_len)
            headers[7]   = self.PadString(headers[7],max_pid_len)
            #
            PrintHeaders(headers)
            #
            connection_count = 0
            #
            try:
                #
                for n in self.network_connections:
                    #
                    ip_version                = self.PadString(n[0],max_ip_version_len)
                    transport_layer_protocol  = self.PadString(n[1],max_transport_layer_len)
                    local_address             = self.PadString(n[2],max_local_addr_len)
                    local_port                = self.PadString(n[3],max_local_port_len)
                    remote_address            = self.PadString(n[4],max_remote_addr_len)
                    remote_port               = self.PadString(n[5],max_remote_port_len)
                    status                    = self.PadString(n[6],max_status_len)
                    pid                       = self.PadString(n[7],max_pid_len)
                    #
                    print("%s %s %s %s %s %s %s %s" % (ip_version,transport_layer_protocol,local_address,local_port,remote_address,remote_port,status,pid))
                    #
                    connection_count += 1
                    #
                    if(connection_count == terminal_height-10):
                        #
                        os.system('cls')
                        #
                        connection_count = 0
                        #
                        PrintHeaders(headers)
                        #
                    time.sleep(.5)
                    #
            except KeyboardInterrupt:
                #
                print("KB INT")
                #
                sys.exit(1)

    def GetUser(self):
        #
        return

    def GetMaxLen(self,subject_list,index):
        #
        max_len = 0
        #
        for entry in subject_list:
            #
            entry = entry[int(index)]
            entry = str(entry)
            #
            if(len(entry) > max_len):
                #
                max_len = len(entry)
                #
        return max_len


    def PadString(self,subject_string,max_len):
        #
        '''
        Type cast in case of integers...
        Yes, I know this is not optimal...
        '''
        #
        subject_string = str(subject_string)
        #
        if(len(subject_string) < max_len):
            #
            while(len(subject_string) < max_len):
                #
                subject_string = subject_string+' '
                #
            return subject_string
            #
        else:
            #
            return subject_string

    def DisplayServices(self):
        #
        def PrintHeaders(header_list):
            #
            for h in header_list:
                #
                print(h,end=' ')
                #
            print()
            #
            for h in headers:
                #
                for c in range(0,len(h)):
                    #
                    print('-',end='')
                    #
                print(' ',end='')
                #
            print()
        #
        while(True):
            #
            self.GetService()
            #
            headers = ['Service','Type','Status','User','PID']
            #
            terminal_dimensions = os.get_terminal_size(1)
            #
            terminal_height = terminal_dimensions[1]
            #
            max_svc_name_len = self.GetMaxLen(self.service_list,0)
            max_type_len     = self.GetMaxLen(self.service_list,1)
            max_status_len   = self.GetMaxLen(self.service_list,2)
            max_svc_user_len = self.GetMaxLen(self.service_list,3)
            max_pid_len      = self.GetMaxLen(self.service_list,4)
            #
            headers[0]   = self.PadString(headers[0],max_svc_name_len)
            headers[1]   = self.PadString(headers[1],max_type_len)
            headers[2]   = self.PadString(headers[2],max_status_len)
            headers[3]   = self.PadString(headers[3],max_svc_user_len)
            headers[4]   = self.PadString(headers[4],max_pid_len)
            #
            PrintHeaders(headers)
            #
            service_count = 0
            #
            try:
                #
                for s in self.service_list:
                    #
                    svc_name = self.PadString(s[0],max_svc_name_len)
                    svc_type = self.PadString(s[1],max_type_len)
                    svc_stat = self.PadString(s[2],max_status_len)
                    svc_user = self.PadString(s[3],max_svc_user_len)
                    svc_pid  = self.PadString(s[4],max_pid_len)
                    #
                    print("%s %s %s %s %s" % (svc_name,svc_type,svc_stat,svc_user,svc_pid))
                    #
                    service_count += 1
                    #
                    if(service_count == terminal_height-10):
                        #
                        os.system('cls')
                        #
                        service_count = 0
                        #
                        PrintHeaders(headers)
                        #
                    time.sleep(.5)
                    #
            except KeyboardInterrupt:
                #
                print("KB INT")
                #
                sys.exit(1)

    def run(self):
        #
        set_dimensions = 'mode 1000,1000'
        #
        os.system(set_dimensions)
        #
        set_color      = 'color 0A'
        #
        os.system(set_color)
        #
        return

if(__name__ == '__main__'):
    #
    monitor = SystemMonitor()
    #
    monitor.run()
    #
    #monitor.DisplayServices()
    #
    #monitor.DisplayNetworkStats()
    #
    monitor.DisplayNetworkConnections()
