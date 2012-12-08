%define     git_name Mandriva-Package-Manager

Name:       mpm
Provides:   mandriva-package-manager
Version:    0.8.3
Release:    2
Summary:    Mandriva Package Manager
Group:      System/Configuration/Packaging
License:    GPLv2
URL:        https://github.com/paulobelloni/Mandriva-Package-Manager
Source0:    %{name}-%{version}.tar.xz
Buildrequires: qt4-linguist >= 4.7.3
Buildrequires: qt4-devel
Buildrequires: imagemagick
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




%changelog
* Tue Aug 30 2011 Paulo Belloni <paulo@mandriva.com> 0.8.3-1
+ Revision: 697494
- Updates to version 0.8.3
- Fix to add ImageMagick as build requirement.
- Fix to put the icons with the correct format in the right place. Thanks neoclust :)
- Setting version to 0.8.2. Please, check NEWS for details
- Adding version 0.8.1. Please, check NEWS for details.
- Upgrading mpm to version 0.7.2. Please, check NEWS for details
- Changes to set MPM 0.7.1 on relese 2011. Check NEWS for details.
- Upgrades to MPM version 0.7.0. Please, check NEWS.

* Fri Jul 01 2011 Paulo Belloni <paulo@mandriva.com> 0.6.1-1
+ Revision: 688514
- Changes to reflect version 0.6.1 of MPM. Please, check NEWS file.

* Wed Jun 22 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.5.1-1
+ Revision: 686695
- Do not obsolete rpmdrake.

* Tue Jun 21 2011 Paulo Belloni <paulo@mandriva.com> 0.5.1-0
+ Revision: 686477
- Changes to set /usr/share/applications/mpm.desktop and /usr/bin/mpm (instead of a link).

* Tue Jun 21 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.5.0-0
+ Revision: 686405
- Add missing BR on qt4-devel

  + Paulo Belloni <paulo@mandriva.com>
    - Please, check https://github.com/paulobelloni/Mandriva-Package-Manager/blob/mpm-0.5.0/NEWS to know more about the changes made for this version. The spec files was changed to include qt4-linguist as build requirement and obsolution of rpmdrake as suggested by neoclust (thanks ;-).

* Sat Jun 11 2011 Paulo Belloni <paulo@mandriva.com> 0.4.0-0
+ Revision: 684226
- Lots of changes on this version. Attaching tarball
- Lots of changes on this version

* Wed Jun 01 2011 Paulo Belloni <paulo@mandriva.com> 0.1.1-1
+ Revision: 682344
- Fixing import path at backend/mdvpkg/mdvpkgqt.py (forget to add the new tar source)
- Fixing import path at backend/mdvpkg/mdvpkgqt.py

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file for rpm5

* Fri May 27 2011 Paulo Belloni <paulo@mandriva.com> 0.1.0-2
+ Revision: 680351
- Including Requires: qt-components-desktop

* Fri May 27 2011 Paulo Belloni <paulo@mandriva.com> 0.1.0-1
+ Revision: 680346
- Creation of the MPM package.
- Created package structure for mpm.

