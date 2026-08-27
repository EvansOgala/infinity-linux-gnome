#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="Infinity_Linux"
iso_label="INFINITY_$(date +%y%m)"
iso_publisher="Infinity Linux Project (Anonymous_947) <https://evansogala.github.io/infinity-linux-web>"
iso_application="Infinity Linux Live/Install Media"
iso_version="2026.9.12-Gnome"
install_dir="infinity"
buildmodes=('iso')
bootmodes=('bios.syslinux'
           'uefi.grub')
pacman_conf="./pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd' '-b' '1M')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--auto-threads=logical' '--long' '-1')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
  ["/etc/sudoers"]="0:0:440"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/root/customize_airootfs.sh"]="0:0:755"
  ["/usr/share/infinity/Scripts/autostart.sh"]="0:0:755"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
  ["/usr/local/bin/ezmaint"]="0:0:755"
  ["/usr/local/bin/infinity-welcome"]="0:0:755"
  ["/usr/local/bin/zram.sh"]="0:0:755"
  ["/usr/local/bin/calamares.sh"]="0:0:755"
  ["/etc/xdg/autostart/calamares.desktop"]="0:0:755"
  ["/etc/skel/.config/autostart/start.desktop"]="0:0:755"
  ["/etc/skel/.config/autostart/infinity-welcome.desktop"]="0:0:755"
  ["/usr/local/bin/grubinstall.sh"]="0:0:755"
  ["/usr/local/bin/ezarch.bios"]="0:0:755"
  ["/usr/local/bin/ezarch.uefi"]="0:0:755"
)
