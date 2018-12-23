#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sgeostat
Version  : 1.0.27
Release  : 12
URL      : https://cran.r-project.org/src/contrib/sgeostat_1.0-27.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sgeostat_1.0-27.tar.gz
Summary  : An Object-Oriented Framework for Geostatistical Modeling in S+
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-sgeostat-lib
BuildRequires : clr-R-helpers

%description
containing functions for variogram estimation, variogram fitting and kriging
  as well as some plot functions. Written entirely in S, therefore works only
  for small data sets in acceptable computing time.

%package lib
Summary: lib components for the R-sgeostat package.
Group: Libraries

%description lib
lib components for the R-sgeostat package.


%prep
%setup -q -c -n sgeostat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521267714

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521267714
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sgeostat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sgeostat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sgeostat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sgeostat|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sgeostat/DESCRIPTION
/usr/lib64/R/library/sgeostat/INDEX
/usr/lib64/R/library/sgeostat/Meta/Rd.rds
/usr/lib64/R/library/sgeostat/Meta/data.rds
/usr/lib64/R/library/sgeostat/Meta/features.rds
/usr/lib64/R/library/sgeostat/Meta/hsearch.rds
/usr/lib64/R/library/sgeostat/Meta/links.rds
/usr/lib64/R/library/sgeostat/Meta/nsInfo.rds
/usr/lib64/R/library/sgeostat/Meta/package.rds
/usr/lib64/R/library/sgeostat/NAMESPACE
/usr/lib64/R/library/sgeostat/R/sgeostat
/usr/lib64/R/library/sgeostat/R/sgeostat.rdb
/usr/lib64/R/library/sgeostat/R/sgeostat.rdx
/usr/lib64/R/library/sgeostat/data/maas.bank.rda
/usr/lib64/R/library/sgeostat/data/maas.rda
/usr/lib64/R/library/sgeostat/help/AnIndex
/usr/lib64/R/library/sgeostat/help/aliases.rds
/usr/lib64/R/library/sgeostat/help/paths.rds
/usr/lib64/R/library/sgeostat/help/sgeostat.rdb
/usr/lib64/R/library/sgeostat/help/sgeostat.rdx
/usr/lib64/R/library/sgeostat/html/00Index.html
/usr/lib64/R/library/sgeostat/html/R.css
/usr/lib64/R/library/sgeostat/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sgeostat/libs/sgeostat.so
/usr/lib64/R/library/sgeostat/libs/sgeostat.so.avx2
/usr/lib64/R/library/sgeostat/libs/sgeostat.so.avx512
