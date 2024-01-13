#!/bin/bash

install_requirements() {
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        echo "Requerimientos instalados correctamente."
    else
        echo "Error: No se encontró el archivo requirements.txt en el directorio actual." >&2
    fi
}

build_binary() {

    if ! command -v pyinstaller &> /dev/null; then
        echo "PyInstaller is not installed. Installing..."
        pip install pyinstaller
        echo "PyInstaller installed successfully."
    else
        echo "PyInstaller is already installed."
    fi

    pyinstaller --onefile -i NONE --name purgerepitedfiles main.py
}


while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -i|--install)
            echo "Installing project requirements..."
            install_requirements
            ;;
        -b|--build)
            echo "Building a binary of the project with pyinstaller..."
            build_binary
            ;;
        -r|--run)
            if [ -f "./dist/purgerepitedfiles" ]; then
                echo "Running app..."
                ./dist/purgerepitedfiles --help
            else
                echo "Executable not found. Building binary..."
                build_binary
                echo "Running app..."
                ./dist/purgerepitedfiles --help
            fi
            ;;
        *)
            echo "Invalid option: $1" >&2
            exit 1
            ;;
    esac
    shift
done