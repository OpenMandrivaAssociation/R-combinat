%global packname  combinat
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.0_8
Release:          2
Summary:          combinatorics utilities
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-8.tar.gz
Source1:          NAMESPACE
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
routines for combinatorics

%prep
%setup -q -c -n %{packname}
cp %{SOURCE1} combinat/

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0_8-1
+ Revision: 778312
- Import R-combinat
- Import R-combinat

