%define module   Eval-Context
%define version    0.07
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Evalute perl code in context wraper
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Eval/%{module}-%{version}.tar.gz
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
BuildRequires: perl(Test::Block)
BuildRequires: perl(Test::Dependencies)
BuildRequires: perl(Test::Distribution)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Spelling)
BuildRequires: perl(Test::Strict)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build::Compat)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module define a subroutine that let you evaluate Perl code in a
specific context. The code can be passed directly as a string or as a file
name to read from. It also provides some subroutines to let you define and
optionally share variables and subroutines between your code and the code
you wish to evaluate. Finally there is some support for running your code
in a safe compartment.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
export LC_ALL=C
make test

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
