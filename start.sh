#!/bin/bash

cd ~/projects/cosecha || exit
source .venv/bin/activate

echo ""
echo "🌱 COSECHA SYSTEM READY"
echo ""
echo "1) Daily log"
echo "2) Weekly summary"
echo "3) Show farm log"
echo "4) Open project folder"
echo "5) Backup farm log"
echo "6) Search farm log"
echo ""

read -p "Choose an option: " choice

case $choice in
  1)
    python ai_summary.py
    ;;
  2)
    python weekly_summary.py
    ;;
  3)
    cat farm_log.txt
    ;;
  4)
    explorer.exe .
    ;;
  5)
    backup_file="farm_log_backup_$(date +%Y-%m-%d_%H-%M-%S).txt"
    cp farm_log.txt "$backup_file"
    echo "Backup created: $backup_file"
    ;;
  6)
    echo "Enter search term:"
    read term
    grep -i "$term" farm_log.txt
    ;;
  *)
    echo "Invalid option"
    ;;
esac