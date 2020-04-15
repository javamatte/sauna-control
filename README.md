# sauna-control
A touch-enabled, Raspberry Pi-based control panel replacement for an indoor, infrared sauna.

## What is this?
A repository for documentation and code for a replacement control panel for an indoor, infrared, 3-person sauna. The display will be a 7" RPi Touchscreen driven by a spare Raspberry Pi 2B+ with USB wifi and bluetooth adapters.

## Why?
Frankly, the built-in control panel was just close enough to usable to incredibly frustrating. It looked fine until you tried to use it, then it quickly became obvious that UX had never been considered in the design of the UI. The equipment functions well, but we'd like it to be smarter... much, much smarter.

The shining light turns out to be the separation between the (admittedly horrible) control panel and the power board. The power board controls the high voltage heater panels, reads the temp sensor, toggles the interior and exterior lights and even handles audible beep feedback for the control panel. It's a 12-pin connector, and I'm fairly certain that I know what most of the pins do at a glance.

## How?
I'm not a UI person, but after casting about for a UI framework that supported Raspberry Pi and various touchscreens, Kivy kept popping up. It feels eerily familiar (like old-school Java Swing layouts bad times) and has a potentially confusing-as-hell overlap between the markup language (.kv files) and the python driving the events/interactions, but what the hell. You only replace a sauna control panel once, right?

## Wat?
No, seriously. The HV electronics and other stuff is on a separate hardware board. You really only need to twiddle 4 pins and read 1 to control the sauna (2 heater and 2 light digital outputs, 1 temp sensor analog input). Everything else is RGB LED gravy at that point (and there will definitely be RGB LEDs).