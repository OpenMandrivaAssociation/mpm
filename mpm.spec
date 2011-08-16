%define     git_name Mandriva-Package-Manager

Name:       mpm
Provides:   mandriva-package-manager
Version:    0.8.2
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
Requires:   mdvpkg >= 0.8.0

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
for i in $(ls -d frontend/images/icons/desktop/*); do
    DIM="${i##*/}"
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/$DIM/apps
    cp $i/mpm.svg %{buildroot}/%{_datadir}/icons/hicolor/$DIM/apps/mpm.svg
done
cp frontend/images/icons/desktop/32x32/mpm.svg %{buildroot}/%{_datadir}/icons/mpm.svg
rm -fr %{buildroot}/%{_datadir}/mandriva/mpm/frontend/images/icons/desktop
I18N_DIR=%{buildroot}/%{_datadir}/mandriva/mpm/frontend/i18n
if [ "$(ls -A $I18N_DIR)" ]; then
    lrelease $I18N_DIR/*ts
    rm -f $I18N_DIR/*ts
fi

%files
%{_bindir}/mpm
%{_datadir}/mandriva/mpm
%{_datadir}/applications/mpm.desktop
%{_datadir}/icons/hicolor/128x128/apps/mpm.svg
%{_datadir}/icons/hicolor/16x16/apps/mpm.svg
%{_datadir}/icons/hicolor/22x22/apps/mpm.svg
%{_datadir}/icons/hicolor/24x24/apps/mpm.svg
%{_datadir}/icons/hicolor/32x32/apps/mpm.svg
%{_datadir}/icons/hicolor/48x48/apps/mpm.svg
%{_datadir}/icons/hicolor/64x64/apps/mpm.svg
%{_datadir}/icons/hicolor/72x72/apps/mpm.svg
%{_datadir}/icons/mpm.svg


