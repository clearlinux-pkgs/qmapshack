#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a0ccc0
#
Name     : qmapshack
Version  : 1.17.1
Release  : 2
URL      : https://github.com/Maproom/qmapshack/archive/V_1.17.1/qmapshack-1.17.1.tar.gz
Source0  : https://github.com/Maproom/qmapshack/archive/V_1.17.1/qmapshack-1.17.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-3.0 MIT
Requires: qmapshack-bin = %{version}-%{release}
Requires: qmapshack-data = %{version}-%{release}
Requires: qmapshack-license = %{version}-%{release}
Requires: qmapshack-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : gdal-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(proj)
BuildRequires : pkgconfig(quazip1-qt5)
BuildRequires : qtbase-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qtscript-dev
BuildRequires : qttools-dev
BuildRequires : qtwebengine-dev
BuildRequires : routino-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Next to all dependencies you need a working GIT, g++ and cmake installation to compile QMapShack on your computer. Clone and compile the code base by:

%package bin
Summary: bin components for the qmapshack package.
Group: Binaries
Requires: qmapshack-data = %{version}-%{release}
Requires: qmapshack-license = %{version}-%{release}

%description bin
bin components for the qmapshack package.


%package data
Summary: data components for the qmapshack package.
Group: Data

%description data
data components for the qmapshack package.


%package doc
Summary: doc components for the qmapshack package.
Group: Documentation
Requires: qmapshack-man = %{version}-%{release}

%description doc
doc components for the qmapshack package.


%package license
Summary: license components for the qmapshack package.
Group: Default

%description license
license components for the qmapshack package.


%package man
Summary: man components for the qmapshack package.
Group: Default

%description man
man components for the qmapshack package.


%prep
%setup -q -n qmapshack-V_1.17.1
cd %{_builddir}/qmapshack-V_1.17.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722539904
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1722539904
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qmapshack
cp %{_builddir}/qmapshack-V_%{version}/3rdparty/alglib/gpl2.txt %{buildroot}/usr/share/package-licenses/qmapshack/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qmapshack-V_%{version}/LICENSE %{buildroot}/usr/share/package-licenses/qmapshack/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qmapshack-V_%{version}/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/qmapshack/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/qmapshack-V_%{version}/msvc_64/LICENSE_Gisinternals.txt %{buildroot}/usr/share/package-licenses/qmapshack/b928376e874da56a850aa233a942c4286915faff || :
cp %{_builddir}/qmapshack-V_%{version}/src/icons/cache/Apache-2.0 %{buildroot}/usr/share/package-licenses/qmapshack/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qmapshack-V_%{version}/src/icons/geocaching/LICENSE.txt %{buildroot}/usr/share/package-licenses/qmapshack/a9e379ed01809d2face7612cb88f38cc79c92bcc || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qmapshack
/usr/bin/qmaptool
/usr/bin/qmt_map2jnx
/usr/bin/qmt_rgb2pct

%files data
%defattr(-,root,root,-)
/usr/share/applications/qmapshack.desktop
/usr/share/applications/qmaptool.desktop
/usr/share/icons/hicolor/128x128/apps/QMapShack.png
/usr/share/icons/hicolor/128x128/apps/QMapTool.png
/usr/share/icons/hicolor/16x16/apps/QMapShack.png
/usr/share/icons/hicolor/16x16/apps/QMapTool.png
/usr/share/icons/hicolor/192x192/apps/QMapShack.png
/usr/share/icons/hicolor/192x192/apps/QMapTool.png
/usr/share/icons/hicolor/22x22/apps/QMapShack.png
/usr/share/icons/hicolor/22x22/apps/QMapTool.png
/usr/share/icons/hicolor/24x24/apps/QMapShack.png
/usr/share/icons/hicolor/24x24/apps/QMapTool.png
/usr/share/icons/hicolor/256x256/apps/QMapShack.png
/usr/share/icons/hicolor/256x256/apps/QMapTool.png
/usr/share/icons/hicolor/32x32/apps/QMapShack.png
/usr/share/icons/hicolor/32x32/apps/QMapTool.png
/usr/share/icons/hicolor/36x36/apps/QMapShack.png
/usr/share/icons/hicolor/36x36/apps/QMapTool.png
/usr/share/icons/hicolor/40x40/apps/QMapShack.png
/usr/share/icons/hicolor/40x40/apps/QMapTool.png
/usr/share/icons/hicolor/42x42/apps/QMapShack.png
/usr/share/icons/hicolor/42x42/apps/QMapTool.png
/usr/share/icons/hicolor/48x48/apps/QMapShack.png
/usr/share/icons/hicolor/48x48/apps/QMapTool.png
/usr/share/icons/hicolor/512x512/apps/QMapShack.png
/usr/share/icons/hicolor/512x512/apps/QMapTool.png
/usr/share/icons/hicolor/64x64/apps/QMapShack.png
/usr/share/icons/hicolor/64x64/apps/QMapTool.png
/usr/share/icons/hicolor/72x72/apps/QMapShack.png
/usr/share/icons/hicolor/72x72/apps/QMapTool.png
/usr/share/icons/hicolor/80x80/apps/QMapShack.png
/usr/share/icons/hicolor/80x80/apps/QMapTool.png
/usr/share/icons/hicolor/8x8/apps/QMapShack.png
/usr/share/icons/hicolor/8x8/apps/QMapTool.png
/usr/share/icons/hicolor/96x96/apps/QMapShack.png
/usr/share/icons/hicolor/96x96/apps/QMapTool.png
/usr/share/pixmaps/QMapShack.png
/usr/share/pixmaps/QMapTool.png
/usr/share/qmapshack/translations/qmapshack_ca.qm
/usr/share/qmapshack/translations/qmapshack_cs.qm
/usr/share/qmapshack/translations/qmapshack_de.qm
/usr/share/qmapshack/translations/qmapshack_es.qm
/usr/share/qmapshack/translations/qmapshack_fr.qm
/usr/share/qmapshack/translations/qmapshack_it.qm
/usr/share/qmapshack/translations/qmapshack_nl.qm
/usr/share/qmapshack/translations/qmapshack_ru.qm
/usr/share/qmaptool/translations/qmaptool_de.qm
/usr/share/qmaptool/translations/qmaptool_es.qm
/usr/share/qmaptool/translations/qmaptool_it.qm
/usr/share/qmaptool/translations/qmaptool_ru.qm
/usr/share/qmt_rgb2pct/translations/qmt_rgb2pct_de.qm

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/QMSHelp.qch
/usr/share/doc/HTML/QMSHelp.qhc
/usr/share/doc/HTML/QMTHelp.qch
/usr/share/doc/HTML/QMTHelp.qhc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qmapshack/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qmapshack/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qmapshack/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qmapshack/a9e379ed01809d2face7612cb88f38cc79c92bcc
/usr/share/package-licenses/qmapshack/b928376e874da56a850aa233a942c4286915faff
/usr/share/package-licenses/qmapshack/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qmapshack.1
/usr/share/man/man1/qmaptool.1
/usr/share/man/man1/qmt_map2jnx.1
/usr/share/man/man1/qmt_rgb2pct.1
