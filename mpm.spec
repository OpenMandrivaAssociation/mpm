%define     git_name Mandriva-Package-Manager

Name:       mpm
Provides:   mandriva-package-manager
Version:    0.7.1
Release:    1
Summary:    Mandriva Package Manager
Group:      System/Configuration/Packaging
License:    GPLv2
URL:        https://github.com/paulobelloni/Mandriva-Package-Manager
Source0:    %{name}-%{version}.tar.xz
Buildrequires: qt4-linguist >= 4.7.3
Buildrequires: qt4-devel
BuildArch:  noarch
Requires:   python-dbus
Requires:   pyside
Requires:   qt-components-desktop
Requires:   mdvpkg = 0.7.0

%description
Mandriva Package Manager - A frontend (QML/PySide based) tool for the mdvpkg
server. It uses DBus to communicate with the server.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/mandriva/mpm
mkdir -p %{buildroot}/%{_bindir}/
cp -R * %{buildroot}/%{_datadir}/mandriva/mpm
cp frontend/bin/mpm %{buildroot}/%{_bindir}
cp frontend/bin/mpm.desktop %{buildroot}/%{_datadir}/applications
rm -fr %{buildroot}/%{_datadir}/mandriva/mpm/frontend/bin
lrelease %{buildroot}/%{_datadir}/mandriva/mpm/frontend/i18n/*ts
rm -f %{buildroot}/%{_datadir}/mandriva/mpm/frontend/i18n/*ts

%files
%{_bindir}/mpm
%{_datadir}/mandriva/mpm
%{_datadir}/applications/mpm.desktop
