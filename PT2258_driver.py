#!/usr/bin/python
# -*- coding: utf-8 -*-

# Autor: Hector Vergara para INSPT - Inove Coding School - Aural Escuela.
# Version: 2.0

import smbus
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
DEVICE_REG_MODE1 = 0x00
import time

'''
NOTE: EXAMPLE!!!


DEVICE_ADDRESS = 0x15      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
'''

ADDRESS_1 = 0x8C
ADDRESS_2 = 0x44 #0x88
ADDRESS_3 = 0x84
ADDRESS_4 = 0x80

MASTER_1dB = 0xE0
MASTER_10dB = 0XD0

CHANNEL_1_1 = 0x90
CHANNEL_1_10 = 0x80

CHANNEL_2_1 = 0x50
CHANNEL_2_10 = 0x40

CHANNEL_3_1 = 0x10
CHANNEL_3_10 = 0x00

CHANNEL_4_1 = 0x30
CHANNEL_4_10 = 0x20

CHANNEL_5_1 = 0x70
CHANNEL_5_10 = 0x60

CHANNEL_6_1 = 0xB0
CHANNEL_6_10 = 0xA0

MUTE = 0xF9
UNMUTE = 0xF8

SYSTEM_RESET = 0xC0 # --> Ver, ¿¿que es esto??

def send_value(address: int = ADDRESS_2, values: list = [UNMUTE]):
    '''
    This function takes the new value and sends it via I2C port.
    '''
    if len(values) == 1:
        #Write a single register
        print('address: ', hex(address))
        print('values: ', int(values[0]))
        bus.write_byte_data(address, 0, int(values[0]))

    elif len(values) > 1:
        #Write an array of registers
        print('address: ', hex(address))
        print('values: ', values)
        bus.write_i2c_block_data(address, 0, values)        
    return -1   

def mute_unmute(mute:bool = False):
    if mute == False:
        send_value(UNMUTE)
    elif mute == True:
        send_value(MUTE)

def change_attenuation(channel:int, level:int, mixer: int = ADDRESS_2):
    '''
    Function for update the attenuation value: 
    transforms the value obtained in the frontend slide to assign it to the VCA.
    '''

    level = abs(level)
    if level > 79:
        level = 79
    tens = level // 10
    unnits = level - (tens * 10)
    
    if channel == 0:
        new_value_1dB = MASTER_1dB + unnits
        new_value_10dB = MASTER_10dB + tens
        # send_value(address = mixer, values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])

    elif channel == 1:
        new_value_1dB = CHANNEL_1_1 + unnits
        new_value_10dB = CHANNEL_1_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])
    
    elif channel == 2:
        new_value_1dB = CHANNEL_2_1 + unnits
        new_value_10dB = CHANNEL_2_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])
    
    elif channel == 3:
        new_value_1dB = CHANNEL_3_1 + unnits
        new_value_10dB = CHANNEL_3_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])
    
    elif channel == 4:
        new_value_1dB = CHANNEL_4_1 + unnits
        new_value_10dB = CHANNEL_4_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])
    
    elif channel == 5:
        new_value_1dB = CHANNEL_5_1 + unnits
        new_value_10dB = CHANNEL_5_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])
    
    elif channel == 6:
        new_value_1dB = CHANNEL_6_1 + unnits
        new_value_10dB = CHANNEL_6_10 + tens
        # send_value(address = mixer,values= [new_value_1dB])
        # send_value(address = mixer,values= [new_value_10dB])
        send_value(address = mixer,  values = [new_value_10dB,new_value_1dB])

if __name__ == '__main__':
    '''
    The main function is used for testing purposes only
    '''
    for i in range(-79,1):
        change_attenuation(channel=1,level= i, mixer=ADDRESS_2)
        time.sleep(0.1)    #sleep for 100m second

import smbus
ADDRESS_1 = 0x8C
ADDRESS_2 = 0x88
ADDRESS_3 = 0x84
ADDRESS_4 = 0x80
# Tomamos como ejemplo el primer PT2258 y el primer canal:
address = ADDRESS_1 
CHANNEL_1_1 = 0x90
CHANNEL_1_10 = 0x80
level = abs(level) # level viene desde el request!!

# Obtenemos las unidades y decenas por separado:
if level > 79:
    level = 79
tens = level // 10
unnits = level - (tens * 10)
# Asignamos los valores de unidades y decenas en dB y creamos una lista
new_value_1dB = CHANNEL_1_1 + unnits
new_value_10dB = CHANNEL_1_10 + tens
values = [new_value_10dB , new_value_1dB ]
# Creamos una conexión al puerto I2C:
bus = smbus.SMBus(1)
# Enviamos los datos:
bus.write_i2c_block_data(address, 0, values)