#!/bin/bash

SRC_FILE="$1"
OUT_FILE="driver_test.ko"

# Try to compile the file using kernel-style gcc flags
gcc -Wall -Wextra -Werror -c "$SRC_FILE" -o temp.o

if [ $? -eq 0 ]; then
  echo "✅ Compilation succeeded."
  exit 0
else
  echo "❌ Compilation failed."
  exit 1
fi
