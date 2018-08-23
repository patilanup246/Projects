import sl4a
import time
import array
import base64
import struct

droid = sl4a.Android()

################## Function ##########################################

def pwm2b(pwmv):
    return struct.pack('I',pwmv)[:2]

def crc_accumulate(b,crcTmp):
    tmp = 0
    tmp = ( b ^ ( crcTmp & 0xff ) ) & 0xff
    tmp = ( tmp ^ ( tmp<<4 ) ) & 0xff
    crcTmp = ( (crcTmp>>8) ^ (tmp<<8) ^ (tmp<<3) ^ (tmp>>4) ) & 0xffff
    return crcTmp


def crc(bstr):
    crcTmp = 0xffff
    for b in bstr :
        crcTmp = crc_accumulate(b,crcTmp)
    #return crcTmp
    #return struct.pack('>I', 0xffff & crcTmp)[:2]
    return struct.pack('I', 0xffff & crcTmp)[:2]


def sgdata(outbyte):

    print("Try to send bytes ...")
    try:

        print("outbyte = ",outbyte)
        #droid.bluetoothWrite(outbyte)
        outstr = base64.b64encode(outbyte).decode("utf-8")
        print("outstr = ",outstr)
        droid.bluetoothWriteBinary(outstr)
        print("Sent!")
        
        time.sleep(0.2)
        
        #Receive byte
        print("Try to receive bytes ...")
        try:

            instr = droid.bluetoothReadBinary(4096).result
            print("Received! Get base64 " , len( instr ) , " byte(s)")
            print("instr = ",instr)
            
            print("Try to decode the receive bytes ...")
            try:
                inbyte = base64.b64decode(bytes(instr,encoding = "utf8"))
                #inbyte = base64.b64decode(instr)
                print("Received! Get " , len( inbyte ) , " byte(s)")
                print("inbyte = ",inbyte)
                for b in inbyte :
                    print(b)
            except:
                print("Decode fail!")
   
        except:
            print("Receive fail!")
 
    except:
        print("Send fail!")

    return inbyte

def CMD_SETPITCH(pwm):
    outmp = b'\x02\x0A' + pwm2b(pwm)
    outmp = b'\xfa' + outmp + crc(outmp)
    sgdata(outmp)
    
print (CMD_SETPITCH(25))