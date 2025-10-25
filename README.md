# Simple Password Manager

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Desktop-lightgrey?logo=windows\&logoColor=white)](#)

A lightweight password manager built with **Python** and **Tkinter / ttkbootstrap**.
Modernized with a sleek UI and added convenience features while keeping it simple, offline, and secure.

---

## Features

*  **Generate secure random passwords** (letters, numbers, symbols)
*  **Copy passwords directly** to your clipboard
*  **Save website credentials** (email + password) locally in `data.json`
*  **Search for saved accounts** with a popup window

  * Popup shows **Email** and **Password**
  * Includes a **Copy Password** button for convenience
*  **Modern UI** using `ttkbootstrap`

  * Clean color-coded buttons (Search, Generate, Add)
  * Centered logo, with automatic fallback if missing
*  Simple, offline, no accounts, no subscriptions

---

## Screenshots

Here you can add your own screenshots of the app.
Example placeholders:

<img width="445" height="432" alt="image" src="https://github.com/user-attachments/assets/f5c432bd-5506-415d-a3bd-3e3380a8404c" />
<img width="445" height="432" alt="image" src="https://github.com/user-attachments/assets/ef736335-f5ca-4216-99b0-dff84fbea0da" />
<img width="359" height="189" alt="image" src="https://github.com/user-attachments/assets/348192b8-5b5a-4955-9e3a-1408c042419d" />

---

## Demo Video


![Demo](videos/video.gif)


---

## Getting Started

### Prerequisites

* Python 3.8+
* Install dependencies:

```bash
pip install pyperclip ttkbootstrap
```

### Run the App

```bash
python main_with_JSON.py
```

---

## Data Storage

All credentials are stored in a local `data.json` file in the same directory as the app.

* If the file doesn’t exist, it will be created automatically.
* No cloud storage, no third-party services, your data stays on your machine.

---

## Tech Stack

* **Python**
* **Tkinter / ttkbootstrap** (modern GUI)
* **JSON** (local storage)
* **pyperclip** (clipboard support)

---

## What’s New in This Version

* Modernized **UI** with themed colors, padding, and clean buttons
* **Popup search results** instead of just messagebox

  * Shows email & password
  * Includes **Copy Password** button
* Logo now has a **placeholder** if `logo.png` is missing
* Slight layout improvements for spacing and alignment

---

## Why I Built This

I didn’t want to rely on paid apps or cloud-based managers.
This project is a small, personal tool:

* Not meant to be fancy
* Not packed with unnecessary features
* Just works when you need it

---

## Disclaimer

This project was built for **personal learning and usage**.
It is **not intended for production use** or as a replacement for professional password managers.

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

