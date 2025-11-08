from pirc522 import RFID
from time import sleep

# 1. Initialize the RFID reader
reader = RFID()

# 2. A list to store the UIDs of tags we've already seen
seen_uids = list()

print("RFID Tag Reader - Initialized")
print("[Press Ctrl+C to stop the script]")

try:
    # 3. Main loop to continuously scan for tags
    while True:
        # Wait for a tag to be present
        reader.wait_for_tag()

        # Request tag information
        (error, tag_type) = reader.request()


        if not error:
            #get the unique UID
            (error, uid) = reader.anticoll()

            if not error:
                if uid not in seen_uids:
                    seen_uids.append(uid)
                    print(f"New tag detected! UID: {uid}")
                else:
                    # If we've seen it before, just print a message
                    print(f"Already detected that tag! UID: {uid}")

        sleep(0.1)

# 4. Handle a clean exit when the user presses Ctrl+C
except KeyboardInterrupt:
    print("\nScript terminated by user.")

finally:
    print("Cleaning up GPIO...")
    reader.cleanup()