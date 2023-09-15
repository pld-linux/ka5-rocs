#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		rocs
Summary:	rocs
Name:		ka5-%{kaname}
Version:	23.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4064bfdbcdea5b00a3bd6ecbe03da413
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5ScriptTools-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	boost-devel >= 1.49
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.0
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rocs is a Graph Theory IDE for everybody interested in designing and
analyzing graph algorithms (e.g., lecturers, students, researchers).
For all these users, Rocs provides an easy to use visual data
structure editor and a powerful scripting engine to execute
algorithms.

Features

- Canvas for Graph Drawing
- IDE for Graph related Programming, using Javascript as it's main
  language, plus the graph library
- Data Structures are extensible from the scripting interface, so you
  can do anything you want.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%defattr(644,root,root,755)
%{_includedir}/rocs
%{_libdir}/librocsgraphtheory.so
