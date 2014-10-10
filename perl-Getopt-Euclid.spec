%define upstream_name	Getopt-Euclid
%define name            perl-%{upstream_name}
%define upstream_version    0.2.3
%define version             %perl_convert_version %{upstream_version}
%define release 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Executable Uniform Command-Line Interface Descriptions
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/upstream_names/by-upstream_name/Getopt/%{upstream_name}-v%{upstream_version}.tar.gz
Buildrequires:  perl(Module::Build)
BuildRequires:  perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Getopt::Euclid uses your program's own documentation to create a command-line
argument parser. This ensures that your program's documented interface and its
actual interface always agree.

%prep
%setup -q -n %{upstream_name}-v%{upstream_version}

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




%changelog
* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 587627
- new version

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 384708
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 268517
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2009.0
+ Revision: 194855
- update to new version 0.2.0
- update to new version 0.2.0

* Fri Jan 18 2008 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-2mdv2008.1
+ Revision: 154592
- forcing rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.1.0-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
+ Revision: 145623
- Imported perl-Getopt-Euclid-0.1.0-1mdv2007.1 into SVN repository.

* Sat Mar 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2007.1
- first mdv release

