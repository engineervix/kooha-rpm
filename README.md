# Kooha RPM Builder

[![RPM Build](https://github.com/engineervix/kooha-rpm/actions/workflows/build.yml/badge.svg)](https://github.com/engineervix/kooha-rpm/actions/workflows/build.yml)

Automated RPM package builder for [Kooha](https://github.com/SeaDve/Kooha), a simple screen recorder. This repository automatically checks for new releases of Kooha and builds RPM packages for Fedora.

## Why?

While Kooha is [available on Flathub](https://flathub.org/apps/io.github.seadve.Kooha), the Flatpak installation includes additional runtime dependencies that may not be necessary for all users. For example, installing the Flatpak version requires:

- GNOME Platform runtime (~364 MB)
- Various GL and video codecs (~350 MB)
- Additional locale files

This RPM package provides a native installation that leverages your system's existing libraries, resulting in a much smaller installation footprint since it only includes the application itself (~2 MB) and uses the dependencies already present on your system.

## How it works

- GitHub Actions checks for new Kooha releases every 12 hours
- When a new release is detected, it:
  1. Updates the version tracking
  2. Builds new RPM packages
  3. Creates a new release with the built packages
  4. Uploads the packages as release artifacts

## Installation

To install the latest version:

1. Download the RPM package from the latest release
2. Enable RPM Fusion repositories if you haven't already:
   ```bash
   sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
   ```
3. Install the package:
   ```bash
   sudo dnf install ./kooha-*.rpm
   ```

The package has been tested and confirmed working on [Fedora Workstation](https://fedoraproject.org/workstation/) 41.

## Manual Build

If you want to build the RPM package manually:

1. Clone this repository
2. Install build dependencies:
   ```bash
   sudo dnf install rpmdevtools rpm-build meson ninja-build appstream \
   gstreamer1-devel gstreamer1-plugins-base-devel gtk4-devel libadwaita-devel
   ```
3. Build the RPM:
   ```bash
   rpmbuild -ba kooha.spec
   ```
