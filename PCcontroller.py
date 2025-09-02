from wakeonlan import send_magic_packet

def PC_on():
    send_magic_packet('ff.ff.ff.ff.ff.ff') #adres MAC komputera
    return "PC turned on"