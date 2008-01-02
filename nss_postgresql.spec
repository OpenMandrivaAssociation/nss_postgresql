%define name nss_postgresql 
%define version 0.6.1
%define release %mkrel 4

Summary: NSS library for postgresql
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ovh.dl.sourceforge.net/sourceforge/authpgsql/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Libraries
Url: http://www.sourceforge.net/projects/authpgsql
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpq-devel
BuildRequires: postgresql-devel

%description
This library provide the capability to have all classical 
users definitions in a PostgreSQL server instead than in the
old plain text files in /etc passwd,group,shadow.

All is done without any trick or something like, simply 
connecting to the nss (name servica switch) facility 
offered by the libc (2.x) as nis and nisplus already did.

All without recompiling or touching any application 
configurations. Just compile and install nss_postgresql 
library and set up a PostgreSQL server.

%prep
%setup -q

%build
%make CFLAGS="%optflags -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot/{%_lib,%_sysconfdir}
install -m755 libnss_pgsql.so.2 %buildroot/%_lib/libnss_pgsql.so.2
install -m644 nss-pgsql.conf %buildroot/%_sysconfdir/nss-pgsql.conf
install -m600 nss-pgsql-root.conf %buildroot/%_sysconfdir/nss-pgsql-root.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc sampleschema README* TODO AUTHORS
/%_lib/libnss_pgsql.so.2
%config(noreplace) %_sysconfdir/*.conf


