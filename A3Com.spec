%include	/usr/lib/rpm/macros.perl
Summary:	A3Com - manipulation of 3Com SuperStack II
Summary(pl):	A3Com - manipulacje 3Com SuperStack II
Name:		A3Com
Version:	0.2.3
Release:	2
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.kernel.org/pub/software/admin/A3Com/%{name}-%{version}.tar.bz2
# Source0-md5:	16133ebf73fe3883b0d46ed88f03377a
URL:		http://www.kernel.org/software/A3Com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A3Com is a set of Perl 5 modules which allow manipulation of 3Com
SuperStack II 3900/9300 and CoreBuilder 3500 LAN switches. Currently
there are modules which can use either the SNMP or telnet interface
to:

- dump the ARP tables
- dump bridge tables
- search switches for a MAC address, IP address, or hostname
- change admin passwords in batch mode
- save and restore switch configurations via SNMP
- upload new firmware via SNMP (batch mode)
- and collect per-port ethernet details like current autonegotiation
  mode and duplex settings
- keep global caches of ARP and bridge tables for fast searches
- keep global ARP history as a merged ARP database

%description -l pl
A3Com to zestaw modu³ów Perla pozwalaj±cych na konfigurowanie switchy
LAN firmy 3Com: SuperStack II 3900/9300 i CoreBuilder 3500. Aktualnie
modu³y te mog± u¿ywaæ interfejsu SNMP lub telnet do:
- wypisania tablic ARP
- wypisania tablic bridgingu
- wyszukiwania adresów MAC, IP lub nazw hostów
- zmiany hase³ administratora w trybie wsadowym
- zapisywania i odtwarzania konfiguracji switchy po SNMP
- przesy³ania nowego firmware'u po SNMP (w trybie wsadowym)
- zbierania dotycz±cych poszczególnych portów informacji takich jak
  aktualny tryb autonegocjacji i duplex
- przechowywania globalnego cache tablic ARP i bridgingu w celu
  szybkiego przeszukiwania
- przechowywania globalnej historii ARP jako po³±czonej bazy danych.

%prep
%setup -q

%build
# Change path for perl:
for i in tools/*; do
	cat $i | sed -e "s/\/usr\/local\/bin/\%{_prefix}\/bin/" > tmp
	mv tmp $i
done
# Change location of config:
for i in A3Com/*; do
	cat $i | sed -e "s/\/usr\/local\/etc/\/etc/" > tmp
	mv tmp $i
done

# Make modules:
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/var/lib/A3Com,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install tools/*		$RPM_BUILD_ROOT%{_bindir}

cat << EOF >$RPM_BUILD_ROOT%{_sysconfdir}/a3com.conf
GLOBALCACHEDIR = /var/lib/A3Com
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG TODO README test.pl
%attr(777,root,root) %dir /var/lib/A3Com
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/a3com.conf
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/A3Com
%{perl_vendorlib}/A3Com/*.pm
