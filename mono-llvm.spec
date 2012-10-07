Summary:	Mono branch of the LLVM optimizing compiler infrastructure
Summary(pl.UTF-8):	Gałąź Mono infrastruktury optymalizującego kompilatora LLVM
Name:		mono-llvm
Version:	2.10
Release:	1
License:	MIT-like
Group:		Development/Tools
Source0:	http://download.mono-project.com/sources/mono-llvm/%{name}-%{version}.tar.gz
# Source0-md5:	38ffa8f19cca5a063607d2e1f2fb5771
URL:		http://www.mono-project.com/Mono_LLVM
BuildRequires:	libstdc++-devel >= 5:3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# use different prefix not to conflict with regular llvm
%define		_prefix		/usr/%{_lib}/mono-llvm
%define		_libdir		%{_prefix}/lib

%description
Mono branch of the LLVM optimizing compiler infrastructure.

%description -l pl.UTF-8
Gałąź Mono infrastruktury optymalizującego kompilatora LLVM.

%package devel
Summary:	Development files for embedding Mono LLVM
Summary(pl.UTF-8):	Pliki programistyczne do osadzania Mono LLVM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 5:3.4

%description devel
Development files for embedding Mono LLVM.

%description devel -l pl.UTF-8
Pliki programistyczne do osadzania Mono LLVM.

%prep
%setup -q -n %{name}-ab69472

%build
install -d obj
cd obj
bash ../%configure \
	--disable-assertions \
	--enable-jit \
	--enable-optimized \
	--enable-shared \
	--disable-static \
	--enable-bindings=none \
	--with-pic

%{__make} \
	OPTIMIZE_OPTION="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C obj -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# see regular llvm
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/{docs,share}
# example
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libLLVMHello.*
# there are shared versions
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib{EnhancedDisassembly,LTO}.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT README.txt
%dir %{_prefix}
%dir %{_bindir}
%attr(755,root,root) %{_bindir}/bugpoint
%attr(755,root,root) %{_bindir}/llc
%attr(755,root,root) %{_bindir}/lli
%attr(755,root,root) %{_bindir}/llvm-ar
%attr(755,root,root) %{_bindir}/llvm-as
%attr(755,root,root) %{_bindir}/llvm-bcanalyzer
%attr(755,root,root) %{_bindir}/llvm-diff
%attr(755,root,root) %{_bindir}/llvm-dis
%attr(755,root,root) %{_bindir}/llvm-extract
%attr(755,root,root) %{_bindir}/llvm-ld
%attr(755,root,root) %{_bindir}/llvm-link
%attr(755,root,root) %{_bindir}/llvm-mc
%attr(755,root,root) %{_bindir}/llvm-nm
%attr(755,root,root) %{_bindir}/llvm-prof
%attr(755,root,root) %{_bindir}/llvm-ranlib
%attr(755,root,root) %{_bindir}/llvm-stub
%attr(755,root,root) %{_bindir}/llvmc
%attr(755,root,root) %{_bindir}/macho-dump
%attr(755,root,root) %{_bindir}/opt
%attr(755,root,root) %{_bindir}/tblgen
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libEnhancedDisassembly.so
%attr(755,root,root) %{_libdir}/libLLVM-2.9svn.so
%attr(755,root,root) %{_libdir}/libLTO.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/llvm-config
%attr(755,root,root) %{_libdir}/libBugpointPasses.so
%attr(755,root,root) %{_libdir}/libprofile_rt.so
%{_libdir}/libCompilerDriver.a
%{_libdir}/libLLVM*.a
%{_libdir}/libUnitTestMain.a
%dir %{_includedir}
%{_includedir}/llvm
%{_includedir}/llvm-c
