%define upstream_name	Getopt-Euclid
%define name            perl-%{upstream_name}
%define upstream_version    0.2.1
%define version             %perl_convert_version %{upstream_version}
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Executable Uniform Command-Line Interface Descriptions
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/upstream_names/by-upstream_name/Getopt/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:  perl(Module::Build)
BuildRequires:  perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Getopt::Euclid uses your program's own documentation to create a command-line
argument parser. This ensures that your program's documented interface and its
actual interface always agree.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


