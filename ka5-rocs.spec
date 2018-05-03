%define		kdeappsver	18.04.0
%define		qtver		5.8.0
%define		kaname		rocs
Summary:	rocs
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	722b474e25d2920ee7afc41ec8387fb8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5ScriptTools-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	grantlee-qt5-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rocs.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rocs
%{_libdir}/librocsgraphtheory.so.0
%{_libdir}/qt5/plugins/rocs
%{_desktopdir}/org.kde.rocs.desktop
%{_datadir}/config.kcfg/rocs.kcfg
%{_iconsdir}/hicolor/128x128/apps/rocs.png
%{_iconsdir}/hicolor/16x16/apps/rocs.png
%{_iconsdir}/hicolor/22x22/apps/rocs.png
%{_iconsdir}/hicolor/32x32/apps/rocs.png
%{_iconsdir}/hicolor/48x48/apps/rocs.png
%{_iconsdir}/hicolor/64x64/apps/rocs.png
%{_iconsdir}/hicolor/scalable/actions/rocsadvancedsetup.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsalignbottom.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsaligncircle.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsalignleft.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsalignmiddle.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsalignright.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsaligntop.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsaligntree.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsalignvmiddle.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsbidirectional.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsdelete.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsedge.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsnode.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsselect.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsunidirectional.svgz
%{_iconsdir}/hicolor/scalable/actions/rocsvisible.svgz
%{_iconsdir}/hicolor/scalable/apps/rocs.svgz
%{_datadir}/kxmlgui5/rocs
%{_datadir}/metainfo/org.kde.rocs.appdata.xml
%{_datadir}/rocs

%files devel
%{_includedir}/rocs
%{_libdir}/librocsgraphtheory.so
