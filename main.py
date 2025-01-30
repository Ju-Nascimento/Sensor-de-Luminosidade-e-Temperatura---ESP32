

#Link para testar o codigo no simulador: https://wokwi.com/projects/399810624918618113

import machine
import ds18x20
import onewire
import time

# Configuração do pino do sensor de luminosidade (LDR)
ldr_pin = machine.Pin(4, machine.Pin.IN)

# Configuração do pino do LED
led_pin = machine.Pin(2, machine.Pin.OUT)

# Configuração do pino do sensor de temperatura
temperature_pin = machine.Pin(15, machine.Pin.IN)

# Configuração do pino do relay do motor
relay_pin_motor = machine.Pin(13, machine.Pin.OUT)

# Inicializar o sensor DS18B20 para o interior
ds_sensor_interior = ds18x20.DS18X20(onewire.OneWire(temperature_pin))

# Escanear para encontrar dispositivos DS18B20
roms_interior = ds_sensor_interior.scan()
print('Found DS devices (Interior):', roms_interior)

# Função para ler o valor do sensor de luminosidade
def read_ldr():
    return ldr_pin.value()

# Função para ler a temperatura do sensor DS18B20
def read_temp():
    ds_sensor_interior.convert_temp()
    time.sleep_ms(750)  # Esperar a conversão da temperatura
    temp = ds_sensor_interior.read_temp(roms_interior[0])
    return temp

# Loop principal
while True:
    # Lê o valor do sensor de luminosidade
    ldr_value = read_ldr()
    print(f"Valor do LDR: {ldr_value}")

    # Lê o valor do sensor de temperatura
    temp_value = read_temp()
    print(f"Temperatura: {temp_value}")

    # Checa as condições e aciona o motor se necessário
    if ldr_value == 0 or temp_value > 23:
        relay_pin_motor.on()
        print("Motor ligado. Abrindo persianas")
        #verificar tempo
    else:
        relay_pin_motor.off()
        print("Motor desligado")

    # Acende o LED se estiver mais claro
    if ldr_value == 0:
        led_pin.on()
    else:
        led_pin.off()

    # Aguarda 5 segundos antes de realizar nova leitura
    time.sleep(5)