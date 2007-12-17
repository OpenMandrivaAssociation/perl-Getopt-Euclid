%define module	Getopt-Euclid
%define name	perl-%{module}
%define version 0.1.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Executable Uniform Command-Line Interface Descriptions
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Getopt/%{module}-v%{version}.tar.bz2
Buildrequires:  perl(Module::Build)
BuildRequires:  perl-version
BuildArch:	    noarch

%description
Getopt::Euclid uses your program's own documentation to create a command-line
argument parser. This ensures that your program's documented interface and its
actual interface always agree.

%prep
%setup -q -n %{module}-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Getopt
%{_mandir}/man3/*


