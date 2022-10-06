import asyncio
import uuid

#imports para connects ao MQTT endpoint no IoT Hub 
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message

CONNECTION_STRING = 'HostName=AzureIoTHubExample.azure-devices.net;DeviceId=thermostat67;SharedAccessKey=4FnSUwOUKYem8ZuZ6hKALA7+3Sd95lWj20lsHkQCfyk=' #chave do dispositivo especifico

value =  #variável que deve passar o valor gerado pelo device

async def main():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        await client.connect()                                                             #estabelecendo conexão

        print("!!device connected!!")

        while True:
            
            message = Message(value)

            #formato da msg 
            message.message_id = uuid.uuid4()
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            # enviar a mensagem 
            print("Sending message: %s" % message.data)
            try:
                await client.send_message(message)
            except Exception as ex:
                print("Error sending message from device: {}".format(ex))
            await asyncio.sleep(1)

    except Exception as iothub_error:
        print("Unexpected error %s from IoTHub" % iothub_error)
        return
    except asyncio.CancelledError:
        await client.shutdown()
        print('Shutting down device client')

# if __name__ == '__main__':
#     print("Press Ctrl-C to exit")
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print('Keyboard Interrupt - sample stopped')