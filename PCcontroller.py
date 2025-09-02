from wakeonlan import send_magic_packet

def PC_on():
    send_magic_packet('4c:cc:6a:f5:59:b6') #adres MAC komputera
    print("wyslano magick packet3")
    return "PC turned on"