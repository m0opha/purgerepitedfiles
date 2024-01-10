#!/bin/bash

if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller no está instalado. Instalando..."
    # Instalar PyInstaller usando pip
    pip install pyinstaller
fi

pyinstaller --onefile -i NONE src/main.py
