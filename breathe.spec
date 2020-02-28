#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : breathe
Version  : 4.13.0.post0
Release  : 9
URL      : https://files.pythonhosted.org/packages/74/83/05c2045d0fc2af9f25d4c7915b78f2109a550c86abe7eb43b3aa36eb5ef0/breathe-4.13.0.post0.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/83/05c2045d0fc2af9f25d4c7915b78f2109a550c86abe7eb43b3aa36eb5ef0/breathe-4.13.0.post0.tar.gz
Summary  : Sphinx Doxygen renderer
Group    : Development/Tools
License  : BSD-3-Clause
Requires: breathe-bin = %{version}-%{release}
Requires: breathe-python = %{version}-%{release}
Requires: breathe-python3 = %{version}-%{release}
Requires: Sphinx
Requires: docutils
Requires: six
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : six

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and
 render `Doxygen <http://www.doxygen.org>`__ xml output.

%package bin
Summary: bin components for the breathe package.
Group: Binaries

%description bin
bin components for the breathe package.


%package python
Summary: python components for the breathe package.
Group: Default
Requires: breathe-python3 = %{version}-%{release}

%description python
python components for the breathe package.


%package python3
Summary: python3 components for the breathe package.
Group: Default
Requires: python3-core
Provides: pypi(breathe)

%description python3
python3 components for the breathe package.


%prep
%setup -q -n breathe-4.13.0.post0
cd %{_builddir}/breathe-4.13.0.post0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582852031
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/breathe-apidoc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
