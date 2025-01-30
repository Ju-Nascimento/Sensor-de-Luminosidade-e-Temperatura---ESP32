# Controle de Persiana Inteligente com Sensor de Luminosidade e Temperatura

Este projeto implementa um sistema de controle de persiana inteligente utilizando um microcontrolador ESP32, sensores de luminosidade (LDR) e temperatura (DS18B20), e um relé para controlar um motor. A persiana é aberta automaticamente quando a luminosidade está baixa ou a temperatura interna excede um limite pré-definido.

## Visão Geral

O sistema monitora continuamente a luminosidade e a temperatura. Se a luminosidade for baixa (indicando que está escuro) ou a temperatura interna for superior a 23°C, o motor é acionado para abrir a persiana. Caso contrário, o motor é desligado, fechando a persiana. Um LED também é aceso quando a luminosidade está baixa.

## Hardware

### Componentes
* Microcontrolador ESP32
* Sensor de luminosidade (LDR)
* Sensor de temperatura DS18B20
* Relé
* Motor
* LED
* Resistores (para o LDR e outros componentes, se necessário)
* Fios e Conectores
* Protoboard ou placa de circuito impresso (PCB)

### Conexões

As conexões entre os componentes e o ESP32 são as seguintes:

* LDR: conectado ao pino 4 do ESP32 (pino analógico).
* LED: conectado ao pino 2 do ESP32.
* Sensor de temperatura DS18B20: conectado ao pino 15 do ESP32.
* Relé do motor: conectado ao pino 13 do ESP32.
* Motor: conectado ao relé.

## Software

### Dependências

* Bibliotecas:
    * `machine` (já incluída no MicroPython)
    * `ds18x20`
    * `onewire`

### Código

O código principal está em `main.py`. Ele inclui as seguintes funcionalidades:

* Inicialização dos pinos dos sensores, LED e relé.
* Leitura dos valores dos sensores de luminosidade e temperatura.
* Acionamento do motor (abertura da persiana) se a luminosidade estiver baixa ou a temperatura for superior a 23°C.
* Desligamento do motor (fechamento da persiana) caso contrário.
* Acendimento do LED se a luminosidade estiver baixa.
* Repetição do processo a cada 5 segundos.

## Como usar

1. Clone este repositório.
2. Conecte os componentes de hardware conforme descrito acima.
3. Copie o código (`main.py`) para o seu ESP32.
4. Execute o código no ESP32.

## Testando o código

Você pode testar o código no simulador Wokwi: [[https://wokwi.com/projects/399810624918618113](https://wokwi.com/projects/399810624918618113)]

## Observações

* Este é um projeto básico. Você pode adicionar funcionalidades como controle manual da persiana, agendamentos, integração com outros sistemas, etc.
* Certifique-se de ajustar os valores de temperatura e luminosidade de acordo com suas preferências e necessidades.

## Contribuindo

Contribuições são sempre bem-vindas. Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está sob a licença MIT.