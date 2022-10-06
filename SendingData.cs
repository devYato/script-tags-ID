using Azure.Messaging.EventHubs.Consumer;
using Microsoft.Azure.Devices;
using Microsoft.Azure.Devices.Client;
using Microsoft.Azure.Devices.Common.Exceptions;
using System;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;

namespace DeviceConnection
{
    public static class NewBaseType
    {
        // /// <your-hub-connection-string> = chave de conexão do IoTHub
        // private const string iotHubConnectionString = "<your-hub-connection-string>";

        /// <your-device-connection-string> = chave de conexão do Device 
        private const string deviceConnectionString = "<your-device-connection-string>";

        public static async Task SendDeviceToCloudMessageAsync(CancellationToken cancelToken)
        {
            var deviceClient = DeviceClient.CreateFromConnectionString(deviceConnectionString);

            var deviceData;// variável que recebe valores do device ---

            while (!cancelToken.IsCancellationRequested)
            {

                var telemetryDataPoint = new
                {
                    Telemetry = deviceData
                };
                var messageString = JsonSerializer.Serialize(telemetryDataPoint);
                var message = new Microsoft.Azure.Devices.Client.Message(Encoding.UTF8.GetBytes(messageString))
                {
                    ContentType = "application/json",
                    ContentEncoding = "utf-8"
                };
                await deviceClient.SendEventAsync(message);
                Console.WriteLine($"{DateTime.Now} > Sending message: {messageString}");

                await Task.Delay(5000);
            }
        }
    }
}

