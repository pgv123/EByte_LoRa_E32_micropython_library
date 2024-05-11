# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E32 LoRa module with MicroPython.
# Sending dictionary to all receivers with CHAN = 23
#
# Note: This code was written and tested using MicroPython on an ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e32 import LoRaE32, Configuration
from machine import UART

from lora_e32_constants import FixedTransmission
from lora_e32_operation_constant import ResponseStatusCode

# Initialize the LoRaE32 module
uart1 = UART(1, baudrate=9600)
lora = LoRaE32('433T20D', uart1, m0_pin=21, m1_pin=22)
code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

# Set the configuration to default values and print the updated configuration to the console
# Not needed if already configured
# configuration_to_set = Configuration('433T20D')
# configuration_to_set.ADDL = 0x02 # Address of this sender no receiver
# configuration_to_set.OPTION.fixedTransmission = FixedTransmission.FIXED_TRANSMISSION
# code, confSetted = lora.set_configuration(configuration_to_set)
# print("Set configuration: {}", ResponseStatusCode.get_description(code))

# Send a dictionary message (fixed)
data = {'key1': 'value1', 'key2': 'value2'}
code = lora.send_broadcast_message(23, data)
# The receiver must be configured with CHAN = 23
print("Send message: {}", ResponseStatusCode.get_description(code))
