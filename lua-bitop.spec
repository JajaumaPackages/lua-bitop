%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           lua-bitop
Version:        1.0.2
Release:        3%{?dist}
Summary:        C extension module for Lua which adds bitwise operations on numbers

Group:          Development/Libraries
License:        MIT
URL:            http://bitop.luajit.org/
Source0:        http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz
Patch0:         lua-bitop-destdir.patch

BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif


%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bitwise
operations on numbers.


%prep
%setup -q  -n LuaBitOp-%{version}
%patch0 -p1 -b .destdir


%build
make %{?_smp_mflags} PREFIX=%{_prefix} LUALIB=%{lualibdir} LUABIN=%{_bindir} CFLAGS="%{optflags} -fPIC"


%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LUALIB=%{lualibdir}


%files
%doc README
%{lualibdir}/*


%changelog
* Mon Aug 4 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-3
- Fix install location

* Tue Jul 29 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-2
- Drop BuildRoot
- Wrap description

* Thu Jun 26 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-1
- Initial package
