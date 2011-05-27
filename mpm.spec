%define     git_name Mandriva-Package-Manager

Name:       mpm
Provides:   mandriva-package-manager
Version:    0.1.0
Release:    %mkrel 1
Summary:    Mandriva Package Manager
Group:      System/Configuration/Packaging
License:    GPLv2
URL:        https://github.com/paulobelloni/Mandriva-Package-Manager
Source0:    %{git_name}-%{version}.tar.xz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:  noarch
Requires:   mdvpkg
Requires:   pyside
Requires:   python-dbus

%description
Mandriva Package Manager - A frontend (QML/PySide based) tool for the mdvpkg
server. It uses DBus to communicate with the server.

%prep
%setup -q -n %{git_name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/mandriva/mpm
mkdir -p %{buildroot}/%{_bindir}/
cp -R * %{buildroot}/%{_datadir}/mandriva/mpm
ln -s %{_datadir}/mandriva/mpm/frontend/bin/mpm %{buildroot}/%{_bindir}/mpm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/mandriva/mpm
%{_bindir}/mpm
