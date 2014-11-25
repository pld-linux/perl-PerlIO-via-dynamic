#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	PerlIO
%define		pnam	via-dynamic
%include	/usr/lib/rpm/macros.perl
Summary:	PerlIO::via::dynamic - dynamic PerlIO layers
Summary(pl.UTF-8):	PerlIO::via::dynamic - dynamiczne warstwy PerlIO
Name:		perl-PerlIO-via-dynamic
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3715f57c346f0c185e24fbc8f580b33b
URL:		http://search.cpan.org/dist/PerlIO-via-dynamic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers. It is
useful when the behavior or the layer depends on variables.

%description -l pl.UTF-8
PerlIO::via::dynamic służy do tworzenia dynamicznych warstw PerlIO.
Jest przydatny kiedy zachowanie lub warstwa zależy od zmiennych.

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
%doc CHANGE*
%{perl_vendorlib}/PerlIO/via/*.pm
%{_mandir}/man3/*
