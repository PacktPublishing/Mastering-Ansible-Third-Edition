# Instructions

Tested on:
- Windows 10 build 17763

Run this command:

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

If installing Linux without the aid of the Windows Store:

    Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile Ubuntu.appx -UseBasicParsing

    Rename-Item Ubuntu.appx Ubuntu.zip
    Expand-Archive Ubuntu.zip C:\WSL\Ubuntu

    C:\WSL\Ubuntu\ubuntu.exe


