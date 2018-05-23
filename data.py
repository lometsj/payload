import subprocess
import shlex
import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys
import os
import signal
import psutil
import json

'''
def get_port():
    """
    return available port.
    """
    cmd = "netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}'"
    procs = os.popen(cmd).readlines()
    #print procs
    for i in range(len(procs)):
        procs[i] = procs[i].rstrip()
    for i in range(8000,65536):
        if str(i) not in procs:
            return i 
'''


def get_payload(binary, exp, times = 5):
    """
    run socat,
    return data.data in tcpstream as payload
    """
    with open('config.json',"r") as f:
        config = json.load(f)
    port = config['port']
    iface = config['iface']
    ans = []


    pcmd = shlex.split('socat tcp-l:' + str(port) + ',fork exec:' + binary)
    pwn = subprocess.Popen(pcmd) # run socat

    for i in range(times):
        outname = binary + '_' + str(i)
        f = open(outname,"w")
        tshark = subprocess.Popen('tshark -i ' + iface + ' -f "tcp dst port ' + str(port) + '" -T fields -e data.data',shell=True,stdout=f,preexec_fn=os.setsid)#run tshark
        time.sleep(2)
        
        ecmd = shlex.split('python '+exp)# run exp
        pay = subprocess.Popen(ecmd)
        time.sleep(2)

        pay.kill()
        f.close()
        os.killpg(os.getpgid(tshark.pid), signal.SIGTERM)# kill chiledren of tshark
    time.sleep(2)

    for i in range(times):
        outname = binary + '_' + str(i)
        #print 'open '+outname
        f = open(outname,'r')
        s = f.readlines()
        res = ''
        for j in s:
            if j <> '\n':
                res += j
        ans.append(res)
        cmd = shlex.split('rm ' + outname)
        subprocess.call(cmd)
    
    pwn.kill()
    #print ('done')
    return ans

def rat(payload_list):
    """
    return the text similarity of input arrary as '[][]'
    """
    times = len(payload_list)
    ra = [[0]*times for i in range(times)]
    for i in range(times):
        for j in range(times):
            ra[i][j] = fuzz.ratio(payload_list[i],payload_list[j])
    return ra
