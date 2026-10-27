#!/usr/bin/env bash

set -u

if ! command -v adb >/dev/null 2>&1; then
  echo "Ошибка: ADB не установлен или не найден в PATH."
  exit 1
fi

if ! adb get-state >/dev/null 2>&1; then
  echo "Телефон не найден."
  echo "Подключи его по USB, включи USB debugging и подтверди запрос на телефоне."
  exit 1
fi

model=$(adb shell getprop ro.product.model | tr -d '\r')
android_version=$(adb shell getprop ro.build.version.release | tr -d '\r')
shell_user=$(adb shell id | tr -d '\r')
su_path=$(adb shell 'command -v su 2>/dev/null || true' | tr -d '\r')

echo "=== RootLab: диагностика устройства ==="
echo "Модель: $model"
echo "Android: $android_version"
echo "Пользователь ADB-оболочки: $shell_user"

if [ -n "$su_path" ]; then
  echo "Команда su найдена: $su_path"
else
  echo "Команда su не найдена в PATH"
fi

echo
echo "Проверка завершена. Никакие настройки телефона не изменялись."
