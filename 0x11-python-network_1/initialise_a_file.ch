#!/bin/bash

touch "$1"; chmod u+x "$1";
echo "#!/usr/bin/python3" >> "$1"
vi "$1"
