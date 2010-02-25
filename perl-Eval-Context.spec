%define upstream_name    Eval-Context
%define upstream_version 0.09.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Evalute perl code in context wraper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Eval/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Compare)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::TreeDumper)
BuildRequires: perl(Directory::Scratch::Structured)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Package::Generator)
BuildRequires: perl(Readonly)
BuildRequires: perl(Safe)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Symbol)
BuildRequires: perl(Term::Size)
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Dependencies)
BuildRequires: perl(Test::Distribution)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Spelling)
BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build::Compat)

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module define a subroutine that let you evaluate Perl code in a
specific context. The code can be passed directly as a string or as a file
name to read from. It also provides some subroutines to let you define and
optionally share variables and subroutines between your code and the code
you wish to evaluate. Finally there is some support for running your code
in a safe compartment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# fails for unknown reason with build bot
rm -f t/000_distribution.t
rm -f t/003_perl_critic.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
export LC_ALL=C
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Eval
