%ifarch aarch64
    %global _lto_cflags %nil
%endif

# Telegram Desktop's constants...
%global appname tdesktop

# Reducing debuginfo verbosity...
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

Name: telegram-desktop
Version: 5.13.1
Release: 0%{?dist}

# Application and 3rd-party modules licensing:
# * Telegram Desktop - GPL-3.0-or-later with OpenSSL exception -- main tarball;
# * tg_owt - BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND MIT AND LicenseRef-Fedora-Public-Domain -- static dependency;
# * rlottie - LGPL-2.1-or-later AND AND FTL AND BSD-3-Clause -- static dependency;
# * cld3  - Apache-2.0 -- static dependency;
# * qt_functions.cpp - LGPL-3.0-only -- build-time dependency;
# * open-sans-fonts  - Apache-2.0 -- bundled font;
# * vazirmatn-fonts - OFL-1.1 -- bundled font.
License: GPL-3.0-or-later AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND MIT AND LicenseRef-Fedora-Public-Domain AND LGPL-2.1-or-later AND FTL AND MPL-1.1 AND LGPL-3.0-only AND OFL-1.1
URL: https://github.com/telegramdesktop/%{appname}
Summary: Telegram Desktop official messaging app
Source0: %{url}/releases/download/v%{version}/%{appname}-%{version}-full.tar.gz

# Telegram Desktop require more than 8 GB of RAM on linking stage.
# Disabling all low-memory architectures.
ExcludeArch: s390x

BuildRequires: cmake(Microsoft.GSL)
BuildRequires: cmake(OpenAL)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(fmt)
BuildRequires: cmake(range-v3)
BuildRequires: tg_owt-devel
BuildRequires: cmake(tl-expected)
BuildRequires: cmake(ada)

BuildRequires: pkgconfig(libsrtp2)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(glibmm-2.68) >= 2.76.0
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libxxhash)
%if 0%{?fedora} < 41
BuildRequires: pkgconfig(openssl)
%endif
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(protobuf-lite)
BuildRequires: pkgconfig(rnnoise)
BuildRequires: pkgconfig(vpx)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-record)
BuildRequires: pkgconfig(xcb-screensaver)
BuildRequires: cmake(absl)

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils

BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  cmake(TDLib)

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: libatomic
BuildRequires: libdispatch-devel
BuildRequires: libqrcodegencpp-devel
BuildRequires: libstdc++-devel
BuildRequires: minizip-compat-devel
BuildRequires: ninja-build
BuildRequires: python3
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: pkgconfig(openh264)

Requires: hicolor-icon-theme
Requires: qt6-qtimageformats%{?_isa}
Recommends: webkitgtk6.0%{?_isa}

# Short alias for the main package...
Provides: telegram = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: telegram%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# Virtual provides for bundled libraries...
Provides: bundled(cld3) = 3.0.13~gitb48dc46
Provides: bundled(kf5-kcoreaddons) = 5.106.0
Provides: bundled(libtgvoip) = 2.4.4~git7c46f4c
Provides: bundled(open-sans-fonts) = 1.10
Provides: bundled(plasma-wayland-protocols) = 1.6.0
Provides: bundled(rlottie) = 0~git8c69fc2
Provides: bundled(vazirmatn-fonts) = 27.2.2
Provides: bundled(cppgir) = 0~git69ef481c
Provides: bundled(minizip) = 1.2.13

%global pth https://raw.githubusercontent.com/huakim/telegram-desktop-patches/refs/heads/master/
Patch0:   %{pth}0002-Disable-saving-restrictions.patch
Patch1:   %{pth}0003-Disable-invite-peeking-restrictions.patch
Patch2:   %{pth}0004-Disable-accounts-limit.patch
#Patch3:   0005-Option-to-disable-stories.patch

%description
Telegram is a messaging app with a focus on speed and security, it’s super
fast, simple and free. You can use Telegram on all your devices at the same
time — your messages sync seamlessly across any number of your phones,
tablets or computers.

With Telegram, you can send messages, photos, videos and files of any type
(doc, zip, mp3, etc), as well as create groups for up to 50,000 people or
channels for broadcasting to unlimited audiences. You can write to your
phone contacts and find people by their usernames. As a result, Telegram is
like SMS and email combined — and can take care of all your personal or
business messaging needs.

%prep
# Unpacking Telegram Desktop source archive...
%autosetup -n %{appname}-%{version}-full -p1

# Unbundling libraries... except minizip
rm -rf Telegram/ThirdParty/{QR,dispatch,expected,fcitx-qt5,fcitx5-qt,hime,hunspell,jemalloc,kimageformats,lz4,nimf,range-v3,xxHash}

# Fix minizip requrement
# sed -i 's|2.0.0|4.0.0|' cmake/external/minizip/CMakeLists.txt

%if 0%{?fedora} >= 41
sed -i "/#include <openssl\/engine.h>/d" Telegram/SourceFiles/core/utils.cpp
%endif

%build
# Building Telegram Desktop using cmake...
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_AR=%{_bindir}/gcc-ar \
    -DCMAKE_RANLIB=%{_bindir}/gcc-ranlib \
    -DCMAKE_NM=%{_bindir}/gcc-nm \
    -DTDESKTOP_API_ID=611335 \
    -DTDESKTOP_API_HASH=d524b414d21f4d37f08684c1df41ac9c \
    -DDESKTOP_APP_USE_PACKAGED:BOOL=ON \
    -DDESKTOP_APP_USE_PACKAGED_FONTS:BOOL=OFF \
    -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION:BOOL=OFF \
    -DDESKTOP_APP_DISABLE_X11_INTEGRATION:BOOL=OFF \
    -DDESKTOP_APP_DISABLE_CRASH_REPORTS:BOOL=ON
sed -i '1s/^/#define QGenericUnixServices QDesktopUnixServices/; s~private/qgenericunixservices_p.h~private/qdesktopunixservices_p.h~g;' Telegram/lib_base/base/platform/linux/base_linux_xdp_utilities.cpp
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md changelog.txt
%license LICENSE LEGAL
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/dbus-1/services/org.telegram.desktop.service
%{_metainfodir}/*.metainfo.xml

%changelog
