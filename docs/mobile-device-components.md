---
layout: default
title: USB multiplexing and mobile-device restore components
---

# USB multiplexing and mobile-device restore components

[Home](../README.md) · [USB and services](usb-and-services.md) · [Restore transport](restore-network.md)

The staging and recovery environments contain USB composite-profile definitions, MobileDevice/restore libraries, CoreDevice and remote-service-discovery components, and ramrod/update paths capable of coordinating device restore. `USBDeviceConfiguration.plist` includes reusable mux, NCM, restore, PTP, audio, keyboard, CarPlay, and camera/display profiles. `standardRestore` includes AppleUSBMux and auxiliary NCM interfaces. The profile list is a configuration vocabulary: it does not show which profile a machine selected or that a USB session occurred.

The RAMDisk's PurpleReverseProxy launch definition names local SOCKS/notification endpoints and a control socket without an explicit loopback node. Its referenced executable is absent from the examined RAMDisk. The [USB/services page](usb-and-services.md) separates socket registration, executable resolution, active listeners, exposure and authentication. None of those runtime states was captured here.

Selected restore-library paths address server selection, TLS options, FDR trust objects, AP tickets, PFX personalization, and IOKit user-client selectors. The [restore-network](restore-network.md) and [PFX pages](firmware-personalization.md) give exact gate and error-path findings. A function named `send` was found delivering to an in-process UARP receiver in one path; the actual device submission occurs at a later staging selector. These relationships explain the workflow without equating a name or import with a physical device transfer. USB traffic, DFU state, peer identity, and successful restore were not observed.
