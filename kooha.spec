Name:           kooha
Version:        2.3.0
Release:        1%{?dist}
Summary:        Elegantly record your screen

License:        GPL-3.0
URL:            https://github.com/SeaDve/Kooha
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  appstream
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       pipewire
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-ugly-free
Requires:       gstreamer1-plugins-bad-free
Requires:       pipewire-gstreamer
Requires:       xdg-desktop-portal
Requires:       gtk4
Requires:       libadwaita

%description
Kooha is a simple screen recorder with a minimal interface. Record your screen
in an intuitive and straightforward way without distractions. Features include
recording microphone and desktop audio, support for WebM, MP4, GIF, and Matroska
formats, and the ability to select a monitor or portion of the screen to record.

%prep
%autosetup -n Kooha-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
appstreamcli validate %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{name}/resources.gresource

%changelog
* Wed Dec 18 2024 GitHub Action <action@github.com> - 2.3.0-1
- Update to version 2.3.0
- For upstream release details: https://github.com/SeaDve/Kooha/releases/tag/v2.3.0
- For more details, see: https://github.com/SeaDve/Kooha/releases/tag/v2.3.0
- This release contains new features and fixes:
- * Area selector window is now resizable
- * Previous selected area is now remembered
- * Logout and idle are now inhibited while recording
- * Video format and FPS are now shown in the main view
- * Notifications now show the duration and size of the recording
- * Notification actions now work even when the application is closed
- * Progress is now shown when flushing the recording
- * It is now much easier to pick from frame rate options
- * Actually fixed audio from stuttering and being cut on long recordings
- * Record audio in stereo rather than mono when possible
- * Recordings are no longer deleted when flushing is cancelled
- * Significant improvements in recording performance
- * Improved preferences dialog UI
- * Fixed incorrect output video orientation on certain compositors
- * Fixed incorrect focus on area selector
- * Fixed too small area selector window default size on HiDPI monitors
- * Updated translations


