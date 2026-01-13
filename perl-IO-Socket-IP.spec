#
# Conditional build:
%bcond_with	tests	# perform "make test" - needs network connection
#
%define		pdir	IO
%define		pnam	Socket-IP
Summary:	IO::Socket::IP - Family-neutral IP socket supporting both IPv4 and IPv6
Name:		perl-IO-Socket-IP
Version:	0.39
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe49e4f6638c55124b4f1fb9ee8fe134
URL:		http://search.cpan.org/dist/IO-Socket-IP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, intended as a replacement for IO::Socket::INET. Most
constructor arguments and methods are provided in a
backward-compatible way.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Socket/IP.pm
%{_mandir}/man3/IO::Socket::IP*.3pm*
