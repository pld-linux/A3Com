%include	/usr/lib/rpm/macros.perl
Summary:	A3Com - manipulation of 3Com SuperStack II
Summary(pl):	A3Com - manipulacje 3Com SuperStack II
Name:		A3Com
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.kernel.org/pub/software/admin/A3Com/%{name}-%{version}.tar.bz2
URL:		http://www.kernel.org/software/A3Com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A3Com is a set of Perl 5 modules which allow manipulation of 3Com
SuperStack II 3900/9300 and CoreBuilder 3500 LAN switches. Currently
there are modules which can use either the SNMP or telnet interface
to:

    - -dump the ARP tables
    - -dump bridge tables
    - -search switches for a MAC address, IP address, or hostname
    - -change admin passwords in batch mode
    - -save and restore switch configurations via SNMP
    - -upload new firmware via SNMP (batch mode)
    - -and collect per-port ethernet details like current autonegotiation
      mode and duplex settings
    - -keep global caches of ARP and bridge tables for fast searches
    - -keep global ARP history as a merged ARP database from

%description -l pl

%prep
%setup -q

%build
for i in tools/*; do
cat $i | sed -e "s/\%{_prefix}\/local\/bin/\%{_prefix}\/bin/" > tmp
	mv tmp $i
done
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install tools/*		$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG TODO README test.pl
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/A3Com/*.pm
