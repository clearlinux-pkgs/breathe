#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : breathe
Version  : 4.21.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/57/ea/f7cb70ca71dac563591baf3f1fc740cbdf689f841ca1a1ffe837227425be/breathe-4.21.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/ea/f7cb70ca71dac563591baf3f1fc740cbdf689f841ca1a1ffe837227425be/breathe-4.21.0.tar.gz
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
Requires: pypi(docutils)
Requires: pypi(six)
Requires: pypi(sphinx)

%description python3
python3 components for the breathe package.


%prep
%setup -q -n breathe-4.21.0
cd %{_builddir}/breathe-4.21.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599769615
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
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
