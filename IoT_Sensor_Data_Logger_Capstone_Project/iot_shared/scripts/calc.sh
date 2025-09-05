#!/bin/bash

echo "Enter first number:"
read a

echo "Enter second number:"
read b

echo "Choose operation (+ or -):"
read op

if [ "$op" = "+" ]; then
    result=$((a + b))
    echo "Result: $result"
elif [ "$op" = "-" ]; then
    result=$((a - b))
    echo "Result: $result"
else
    echo "Invalid operation"
fi
