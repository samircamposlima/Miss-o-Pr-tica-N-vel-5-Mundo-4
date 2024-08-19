# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import uuid
import time
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import Message


def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print("IoTHub Device Client Recurring Telemetry Sample")
    print("Press Ctrl+C to exit")
    try:
        # Connect the client.
        device_client.connect()

        # Send recurring telemetry
        i = 0
        while True:
            i += 1
            msg = Message("test wind speed " + str(i))
            msg.message_id = uuid.uuid4()
            msg.correlation_id = "correlation-1234"
            msg.custom_properties["tornado-warning"] = "yes"
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"
            print("sending message #" + str(i))
            device_client.send_message(msg)
            time.sleep(2)
    except KeyboardInterrupt:
        print("User initiated exit")
    except Exception:
        print("Unexpected exception!")
        raise
    finally:
        device_client.shutdown()


if __name__ == "__main__":
    main()
