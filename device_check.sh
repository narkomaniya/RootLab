#!/usr/bin/env bash

if ! command -v adb >/dev/null 2>&1; then
  echo "ADB пока не установлен."
  echo "Когда установим Android Platform Tools, скрипт сможет проверить телефон."
  exit 0
fi

echo "Подключённые Android-устройства:"
adb devices
