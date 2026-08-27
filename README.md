# Infinity Linux
### version 2026.9.12
<h2><b>Infinity Linux</b> is a lightweight Arch Linux-based distribution focused on <b>speed, flexibility, compatibility, and ease of installation.</b></h2><br />

<h4>It uses:</h4>

- Arch Linux base
- Calamares graphical installer
- BIOS and UEFI boot support
- KDE Plasma desktop environment
- PipeWire audio stack
- Flatpak support
- ZRAM swap utilization
- New addition - GNOME Edition

## Repository Layout
- etc/            (System configuration)
- usr/            (Wallpapers, icons, launchers, branding)
- grub/           (GRUB bootloader configuration)
- syslinux/       (BIOS bootloader configuration)
- efiboot/        (UEFI bootloader configuration)
- opt/ezrepo/     (Local package repository)
- packages.x86_64 (Package list)
- profiledef.sh   (ArchISO profile configuration)
- steps.sh        (Automated build script)

## Requirements

### Build host:

- Arch Linux
- Root access
- archiso
- mkinitcpio-archiso

### Required packages:
```bash
sudo pacman -S archiso mkinitcpio-archiso
```

### Building

Clone the repository:
```bash
git clone https://github.com/EvansOgala/infinity-linux.git
cd infinity-linux
```
Run the build script:
```bash
sudo ./steps.sh
```
<b>The generated ISO will appear in:</b>

out/

### Boot Support

<b>Supported:</b>

- Legacy BIOS (syslinux / grub)
- UEFI (GRUB / systemd-boot)

### Desktop Environment

<b>Desktop Environments ccurrently in use:</b>

- KDE Plasma
- GNOME

<b>Display manager:</b>

- SDDM (KDE)
- GDM (GNOME)

### Verification

Generate checksums:
```bash
sha256sum *.iso > SHA256SUMS
```
<b>Verify:</b>
```bash
sha256sum -c SHA256SUMS
```
See LICENSE file for details.

### Status

<b>Current status:</b>

**First stable release.**

>>>>>>> 13f8588 (Fourth Infinity Linux release)
