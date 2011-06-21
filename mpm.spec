%define     git_name Mandriva-Package-Manager

Name:       mpm
Provides:   mandriva-package-manager
Version:    0.5.0
Release:    0
Summary:    Mandriva Package Manager
Group:      System/Configuration/Packaging
License:    GPLv2
URL:        https://github.com/paulobelloni/Mandriva-Package-Manager
Source0:    %{name}-%{version}.tar.xz
Buildrequires: qt4-linguist >= 4.7.3
BuildArch:  noarch
Requires:   python-dbus
Requires:   pyside
Requires:   qt-components-desktop
Requires:   mdvpkg >= 0.6.3
Obsoletes: rpmdrake

%description
Mandriva Package Manager - A frontend (QML/PySide based) tool for the mdvpkg
server. It uses DBus to communicate with the server.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/mandriva/mpm
mkdir -p %{buildroot}/%{_bindir}/
cp -R * %{buildroot}/%{_datadir}/mandriva/mpm
ln -s %{_datadir}/mandriva/mpm/frontend/bin/mpm %{buildroot}/%{_bindir}/mpm
lrelease %{buildroot}/%{_datadir}/mandriva/mpm/frontend/i18n/*ts
rm -f %{buildroot}/%{_datadir}/mandriva/mpm/frontend/i18n/*ts

%files
%{_datadir}/mandriva/mpm
%{_bindir}/mpm
