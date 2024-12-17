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
