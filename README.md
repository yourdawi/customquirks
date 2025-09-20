# Custom ZHA Device Quirks Collection

This repository contains custom ZHA device handlers (quirks) to enable support for Zigbee devices that are not fully supported by the official ZHA integration yet.

## Included Quirks

| Device Manufacturer | Model    | Description                                |
|---------------------|----------|--------------------------------------------|
| HOBEIAN             | ZG-102Z  | Zigbee door/window contact sensor with Tuya manufacturer-specific cluster support |

## Purpose

Some Zigbee devices, especially certain Chinese-made models, have vendor-specific behaviors and clusters that are not covered by default in ZHA. These quirks extend ZHA to properly handle such devices, exposing their sensor entities and features correctly.

## Installation

1. Copy all quirk files (e.g. `tuya_zg_102z_quirk.py`) into your Home Assistant configuration folder, for example `/config/zha_quirks/`.
2. Enable custom quirks in your `configuration.yaml`:

