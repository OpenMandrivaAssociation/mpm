%define     git_name Mandriva-Package-Manager

Summary:	Mandriva Package Manager
Name:		mpm
Version:	0.8.3
Release:	9
Group:		System/Configuration/Packaging
License:	GPLv2
Url:		https://github.com/paulobelloni/Mandriva-Package-Manager
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
Buildrequires:	qt4-linguist >= 4.7.3
Buildrequires:	qt4-devel
Buildrequires:	imagemagick
Requires:	python-dbus
Requires:	pyside
Requires:	qt-components-desktop
Requires:	mdvpkg >= 0.8.0
Provides:	mandriva-package-manager

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
    mkdir -p %{buildroot}/%{_iconsdir}/hicolor/$DIM/apps
    convert -background none $i/mpm.svg \
        %{buildroot}/%{_iconsdir}/hicolor/$DIM/apps/mpm.png
done
cp frontend/images/icons/desktop/32x32/mpm.svg \
       %{buildroot}/%{_iconsdir}/mpm.png
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/scalable/apps
cp frontend/images/icons/desktop/72x72/mpm.svg \
       %{buildroot}/%{_iconsdir}/hicolor/scalable/apps
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
%{_iconsdir}/hicolor/128x128/apps/mpm.png
%{_iconsdir}/hicolor/16x16/apps/mpm.png
%{_iconsdir}/hicolor/22x22/apps/mpm.png
%{_iconsdir}/hicolor/24x24/apps/mpm.png
%{_iconsdir}/hicolor/32x32/apps/mpm.png
%{_iconsdir}/hicolor/48x48/apps/mpm.png
%{_iconsdir}/hicolor/64x64/apps/mpm.png
%{_iconsdir}/hicolor/72x72/apps/mpm.png
%{_iconsdir}/mpm.png
%{_iconsdir}/hicolor/scalable/apps/mpm.svg

