# AstroPi Project

This project is my first experience with Python programming and is part of my participation in the AstroPi project. The aim is to collect environmental data from the International Space Station (ISS) using the Sense HAT.

## Overview

The program gathers temperature, pressure, and humidity data from the Sense HAT sensors, and logs this information into a CSV file (`dades.csv`). The data collection process runs for a specified duration, recording sensor measurements at regular intervals.

## Features

- Displays messages on the Sense HAT LED matrix to indicate program status.
- Collects and logs sensor data: temperature, pressure, humidity, and accelerometer readings.
- Outputs data to a CSV file for further analysis.

## Requirements

- Raspberry Pi with Sense HAT
- Python 3.x
- Sense HAT library

## Usage

1. Set up your Raspberry Pi with the Sense HAT module.
2. Run the `main.py` script to start collecting data.
3. Data is saved to `dades.csv` in the specified directory.

## Acknowledgments

This project is inspired by the AstroPi initiative, which allows students to run code on the ISS and learn about programming and space science.
