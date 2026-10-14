# Infinity Linux

[![Download infinity-linux](https://img.shields.io/sourceforge/dt/infinity-linux.svg)](https://sourceforge.net/projects/infinity-linux/files/latest/download)

<h2><b>Infinity Linux</b> is a lightweight Arch Linux-based distribution based on Ezarcher, built for <b>performance, freedom, and control.</b></h2><br />
<h3>The future is open.</h3>

[![Download infinity-linux](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/infinity-linux/files/latest/download)

<h4> Features: </h4>
- KDE Plasma desktop environment
- Calamares installer
- NetworkManager networking
- PipeWire audio stack
- Flatpak support
- Plasma Vault integration
- BIOS and UEFI boot modes
- Large software selection included in the live environment

## Repository Layout
etc/            System configuration
usr/            Wallpapers, icons, launchers, branding
grub/           GRUB bootloader configuration
syslinux/       BIOS bootloader configuration
efiboot/        UEFI bootloader configuration
opt/ezrepo/     Local package repository
packages.x86_64 Package list
profiledef.sh   ArchISO profile configuration
steps.sh        Automated build script
Requirements

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

- Legacy BIOS
- UEFI

### Desktop Environment

<b>Default desktop:</b>

- KDE Plasma
- GNOME (quarterly release, it's best u use Plasma instead)

<b>Display manager:</b>

- SDDM
- GDM (for GNOME)

### Kernel

<b>Infinity Linux uses:</b>

- linux

A specialized infinity linux kernel is coming soon.

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

<b>Send any bugs found to ripgoku831@gmail.com</b>

### Status

<b>Current status:</b>

**Stable release.**
>>>>>>> 2fe81a8 (Stable Infinity Linux release)
