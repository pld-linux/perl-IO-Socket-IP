#
# Conditional build:
%bcond_with	tests	# test suite (needs network connection)
#
%define		pdir	IO
%define		pnam	Socket-IP
Summary:	IO::Socket::IP - Family-neutral IP socket supporting both IPv4 and IPv6
Summary(pl.UTF-8):	IO::Socket::IP - niezależne od rodziny gniazdo IP, obsługujące IPv4 i IPv6
Name:		perl-IO-Socket-IP
Version:	0.44
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/IO/PEVANS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d0908e82db87a1921ebfd88139cb9d7
URL:		https://metacpan.org/dist/IO-Socket-IP
BuildRequires:	perl-Module-Build >= 0.4004
BuildRequires:	perl-devel >= 1:5.14
%if %{with tests}
BuildRequires:	perl(Test2::V0)
BuildRequires:	perl-Socket >= 1.97
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, intended as a replacement for IO::Socket::INET. Most
constructor arguments and methods are provided in a
backward-compatible way.

%description -l pl.UTF-8
Ten moduł udostępnia niezależny od protokołu sposób używana gniazd
IPv4 oraz IPv6; jest pomyślany jako zamiennik dla IO::Socket::INET.
Większość argumentów konstruktora i metod jest zgodna wstecznie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

./Build

%if %{with tests}
./Build test
%endif

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Socket/IP.pm
%{_mandir}/man3/IO::Socket::IP*.3pm*
