# Raspberry Pi 3B+ RFID Project

A side project exploring RFID technology with a Raspberry Pi 3B+.

## 📋 Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Wiring Diagram](#wiring-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Project Status](#project-status)
- [License](#license)

## 🛠️ Hardware requirements

- Raspberry Pi 3B+
- RFID RC522 Module (or specify your model)
- RFID Tags/Cards
- Jumper wires (Female-to-Female, or potato board)
- Power supply for Raspberry Pi

## 💻 Software Requirements

- Raspberry Pi OS (Raspbian)
- Python 3.x
- SPI enabled on Raspberry Pi

## 🔌 Wiring Diagram

| RFID RC522 Pin | Raspberry Pi Pin | Pin Number |
|----------------|------------------|------------|
| SDA            | GPIO 8 (CE0)     | Pin 24     |
| SCK            | GPIO 11 (SCKL)   | Pin 23     |
| MOSI           | GPIO 10 (MOSI)   | Pin 19     |
| MISO           | GPIO 9 (MISO)    | Pin 21     |
| IRQ            | Not Connected    | -          |
| GND            | Ground           | Pin 6      |
| RST            | GPIO 25          | Pin 22     |
| 3.3V           | 3.3V             | Pin 1      |

## 📦 Installation

### 1. Enable SPI Interface

```bash
sudo raspi-config
```

Navigate to: `Interfacing Options` → `SPI` → `Enable`

### 2. Update System

```bash
sudo apt-get update
sudo apt-get upgrade
```

### 3. Install Python Libraries

```bash
sudo apt-get install python3-dev python3-pip
sudo pip3 install spidev
sudo pip3 install mfrc522
```

### 4. Clone This Repository

```bash
git clone https://github.com/Sintaxytb/PI-project.git
cd PI-project
```

## 🚀 Usage

### Basic Read Example

```bash
python3 read_rfid.py
```

Place an RFID tag near the reader to see the UID displayed.

## 🐛 Troubleshooting

### Issue: RFID reader not detected

**Solution:**
- Verify SPI is enabled: `lsmod | grep spi`
- Check wiring connections
- Ensure 3.3V power (NOT 5V - this can damage the module)

### Issue: No response when scanning tags

**Possible causes:**
- Incorrect wiring
- SPI not enabled
- Wrong GPIO pins in code
- Damaged RFID module

### Issue: Permission errors

**Solution:**
```bash
sudo usermod -a -G spi,gpio pi
sudo reboot
```

## 📊 Project Status

⚠️ **Currently not working** - Troubleshooting in progress

### Known Issues:
- [ ] RFID reader not responding
- [ ] GPIO pins not cleaning after ending. Seems to be a requirements problem.

### To Do:
- [ ] Fix connection issues
- [ ] Implement tag writing functionality
- [ ] Add database logging
- [ ] Create web interface


## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---